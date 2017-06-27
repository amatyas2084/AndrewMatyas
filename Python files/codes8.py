'''
Author: Andrew Matyas
Date: 4/13


Description:
<summary of this program>
'''
from bs4 import BeautifulSoup
import numpy as np
import requests
import zlib
import os
import json


def get_soup(url=None, fname=None, gzipped=False):
    """ If the filename is not None, read the file, pass its contents to
        the BeautifulSoup constructor, and return the resulting object.
        Otherwise, if the url is None, raise a RuntimeError with the
        message 'Either url or filename must be specified.' If it is not
        None, send a get request to the server. If the response content
        is zipped (third parameter), unzip it. Pass the content to the
        BeautifulSoup constructor and return the resulting object.

        Args:
            url -- (String) location to be scraped.
            fname -- (String) a filename to be read.
            gzipped -- (Boolean) Is content zipped?

        returns:
            a BeautifulSoup object
    """
    
    if fname is not None:
        file = open(fname)
        soup = BeautifulSoup(file)
        file.close
        return soup
    
    if url is None:
        raise RuntimeError('Either url or filename must be specified.')
    
    page = requests.get(url)
    if gzipped:
        content = zlib.decompress(page.content, 16+zlib.MAX_WBITS)
        soup = BeautifulSoup(content)
        return soup
    soup = BeautifulSoup(page.content)
    return soup


def save_soup(fname, soup):
    """ This function saves a textual representation of a soup object.

    Args:
        fname -- (String) name for saved file
        soup -- (BeatifulSoup) object to save

    return:
        n/a
    """

    f = open(fname, 'w+')
    f.write(repr(soup))


def scrape_and_save():
    """ This function scrapes a series of addresses, soupifies the
        content, and stores a textual representation of these objects in
        the files 'wrcc_pcpn.html', 'wrcc_mint.html', and 'wrcc_maxt.html',

    Args:
        None
    returns:
        n/a
    """

    url1 = 'http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+pcpn+none+msum+5+01+F'
    save_soup('wrcc_pcpn.html', get_soup(url=url1))
    url2 = 'http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+mint+none+mave+5+01+F'
    save_soup('wrcc_mint.html', get_soup(url=url2))
    url3 = 'http://www.wrcc.dri.edu/WRCCWrappers.py?sodxtrmts+028815+por+por+maxt+none+mave+5+01+F'
    save_soup('wrcc_maxt.html', get_soup(url=url3))

def is_num(check):
    """ This Boolean function takes a string and determines whether or
    not it represents a number (either integer or floating point).

    Args:
        check -- (String) to be checked for number status

    returns:
        a boolean value representing whether or not the provided value
        is a string
    """
    try:
        i = int(check)
        return True
    except :
        try:
            i = float(check)
            return True
        except:
            return False

def load_lists(base, flag):
    """ This function takes a soup object and a flag as arguments and
    returns a list of lists containing the useful data in the soup
    object. The soup object contains an html parse tree that describes
    a table of data.

    Args:
        base -- (Soup) object containing data to be read
        flag -- (int) flag to signify replacements

    returns:
        data from webpage as list
    """
    
    content = []
    for rows in base.find_all("tr"):
        if len(rows.find_all("td")) < 2:
            break
        else:    
            pos = 0
            row = []
            for cell in rows.find_all("td"):
                if is_num(str(cell.get_text())):
                    if pos == 0:
                        row.append(int(cell.get_text()))
                    else:
                        row.append(float(cell.get_text()))
                if cell.get_text() == '-----':
                    row.append(flag)
                pos += 1
            if len(row) > 0:
                content.append(row)
    
    lists = []
    first = True 
    for line in content:
        if first:
            for num in line:
                lists.append([num])
            first = False
        else:
            for i in range(len(line)):
                lists[i].append(line[i])
    return lists


def replace_na(fix_list, row, column, flag, precision=5):
    """ Replaces missing data with averages of nearby data. It averages
    +- 5-columns worth of data. All additional mising data is ignored.

    Args:
        fix_list -- (list) to be altered
        row -- (int) row position
        column -- (int) column position
        flag -- (int) number to be changed
        precision -- (int) 
    
    returns:
        average datapoint
    """
    if column-5 >0:
        surround = [x for x in fix_list[row][column+1:column+6] if x !=flag] + [y for y in fix_list[row][column-5:column] if y != flag]
    else:
        surround = [x for x in fix_list[row][column+1:column+6] if x !=flag] + [y for y in fix_list[row][0:column] if y != flag]    
    return round(sum(surround)/len(surround),precision)    
    

def clean_data(data, flag,precision=5):
    """ This function traverses the list of lists and every time it finds the flag, it calls replace_na to replace the flag.
    Args:
        repl -- (list of lists) with a position to replace
        flag -- (int) to be replaced
    returns:
        replaced list
    """
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == flag:
                data[i][j] = replace_na(data, i, j, flag,precision)

def recalculate_annual_data(data, averages=False,precision=5):
    """ This function recalculates annual data now that we have cleaned it.

    Args:
        data -- (list of lists) data with row to be replaced
        averages -- (boolean) True if annual should be averages,
                              False if annual should be total

    returns:
        n/a
    """
    for i in range(len(data[0])):
        total = 0
        for j in range(1, len(data) - 1):
            total += data[j][i]
            if averages: 
                data[-1][i] = round(round(total,precision) / j,precision)
            else: 
                data[-1][i] = round(total,precision)
        total = 0


def clean_and_jsonify(fnames, flag,precision=5):
    """ This function cleans and jsonifies multiple files. It will get a
    soup object, transform it into a list of lists, clean the list,
    recalculate the annual data, and store a json object in file.

    Args:
        fnames -- (list of Strings) filenames to be processed
        flag -- (int) the flag for processing
    """
    for f in fnames:
        soup = get_soup(fname=f)
        data = load_lists(soup, flag)
        clean_data(data,flag,precision)
        if 'max' in f or 'min' in f:
            recalculate_annual_data(data,True,precision)
        else:
            recalculate_annual_data(data,False,precision)
        new = open(f[0:-5]+".json",'w')
        json.dump(data,new)
        new.close()
        


def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    
    fnames= ['wrcc_pcpn.html','wrcc_mint.html','wrcc_maxt.html']
    clean_and_jsonify(fnames,-999,2)
    
    
    
    
    
if __name__ == '__main__':
    main()