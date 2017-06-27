'''
Author: Andrew Matyas
Date: 4/6

Description:
<summary of this program>
'''
from bs4 import BeautifulSoup
import requests
import zlib
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
    # do we have a filename?
    if fname is not None:
        file = open(fname)
        soup = BeautifulSoup(file)
        file.close
        return soup
    # if no filename or url, raise error
    if url is None:
        raise RuntimeError('Either url or filename must be specified.')
    # read from url
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


def main():
    """ Check the current directory for any one of the files that scrape_and_save creates. If it is not there, print '---- scraping and saving ----' and scrape and save the addresses.
    
    Args:
        n/a

    returns:    
        n/a
    """
    files = os.listdir()
    for file in ['wrcc_pcpn.html', 'wrcc_mint.html', 'wrcc_maxt.html']:
        if file not in files:
            print("---- scraping and saving ----")
            scrape_and_save()
            break


  
if __name__ == '__main__':
    main()