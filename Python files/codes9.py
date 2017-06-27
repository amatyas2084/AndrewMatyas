'''
Author: Andrew Matyas
Date: 4/19

Description:
<summary of this program>
'''
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import zlib
import json
import os


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



def get_panda(fname):
    """ This function takes a string representing a filename, which
    contains a json object representing a list of lists. Returns a
    DataFrame that has the same data as the list with row labels (index)
    that are the three-letter abbreviations for the months and the year
    ['Jan', 'Feb', ..., 'Dec', 'Ann'] and column labels (columns) that
    are integers representing years [1894, 1895, ...].
    
    Args:
        fname -- (String) a filename

    returns:
        A DataFrame of organized json data
    """
    f = open(fname).read()
    j_data = json.loads(f)
    index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Ann']
    columns = []
    for i in range(1894, 2009):
        columns.append(i)
    data = np.zeros((len(index), len(columns)))
    for i in range(0,len(j_data) - 1):
        for j in range(len(j_data[i])):
            data[i][j] = j_data[i + 1][j]
    frame = DataFrame(data, index, columns)
    return frame

def get_stats(df):
    """ This function takes a DataFrame, calculates the statistics and returns DataFrame with them.

    Args:
        df -- (DataFrame) to be summarized

    returns:
        new DataFrame statistical summary of df
    """
    index = ['mean','sigma','s','r']
    columns = list(df.index)
    data = np.zeros((len(index), len(columns)))
    for i in range(len(df.index)):
        row = Series(df.values[i])
        
        m = row.mean()
        data[0][i] = m
        
        sig = df.values[i].std()
        data[1][i] = sig
        
        s = row.std()
        data[2][i] = s
        
        col = Series(df.columns)
        
        r = row.corr(col)
        data[3][i] = r
    nf = DataFrame(data, index, columns)
    return nf

def print_stats(fname):
    """ This function prints the following header:
        '----- Statistics for <filename> -----\n'. 
    Then it creates a DataFrame from the data in the file. It then prints
    a DataFrame containing a statistical summary of that data. Then prints
    a blank line.

    Args:
        fname -- (String) a filename
    returns:
        n/a
    """
    print('----- Statistics for ' + fname + ' -----\n')
    print(get_stats(get_panda(fname)))
    print()

def smooth_data(df, precision = 5):
    """ This function replaces each data point of a DataFrame with the
    11-year average of the surrounding data, including the data point itself.
    Args:
        df -- (DataFrame) raw data

    returns:
        a new DataFrame of average values
    """
    index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
             'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Ann']
    columns = []
    for i in range(1894, 2009):
        columns.append(i)
    data = np.zeros((len(index), len(columns)))
    nf = DataFrame(data, index, columns)
    for i in range(len(df.index)):
        row = df.iloc[i:i+1,:]
        arr = []
        for j in range(len(df.columns)):
            if j < 5:
                sub = df.iloc[i:i+1,:j + 6].values
            else:
                sub = df.iloc[i:i+1,j - 5:j + 6].values
            avg = sub.mean()
            arr.append(avg)
      
        for k in range(len(arr)):
            nf.iloc[i:i+1,k:k+1] = arr[k]
    return nf


def make_plot(fname, mon=None):
    """ This function makes a DataFrame from a file and smooths the data.
    If the month argument is none, it plots the smoothed data for each
    month on an appropriate subplot. If the month argument isn't None,
    it plot just that month's data and its smoothed data.

    Args:
        fname -- (String) a filename
        mon -- (String) an abbreviation for a month, default is None
    """
    df = get_panda(fname)
    smooth = smooth_data(df)
    trans = df.T
    smooth_df = smooth.T
    if mon is None:
        p = trans.plot(subplots=True, legend=None, color='g', yticks=[], title=fname)

        for i in range(len(smooth_df.columns)):
            smooth_df.iloc[:,i].plot(ax=p[i])
            p[i].set_ylabel(smooth.index[i])
    else:
        raw_month = Series(trans.ix[:,mon])
        t = str(fname + ": " + mon)
        p = raw_month.plot(legend=None, title=t)
        s = Series(smooth_df.ix[:,mon])
        s.plot(color='g')


def main():
    """ Check the current directory for any one of the files that
    scrape_and_save creates. If it is not there, print '---- scraping
    and saving ----' and scrape and save the addresses.

    Args:
        n/a

    returns:
        n/a
    """
    fnames = ['wrcc_pcpn.html','wrcc_mint.html', 'wrcc_maxt.html']
    clean_and_jsonify(fnames, -999)
    for fname in fnames:
        json_fname = fname.split('.')[0] + '.json'
        print_stats(json_fname)
        make_plot(json_fname)
    plt.figure()
    make_plot(fnames[0].split('.')[0] + '.json', 'Jan') 
    input('Enter to end:')
if __name__ == '__main__':
    main()