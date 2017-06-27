'''
Author: Andrew Matyas
Date: 2/5


Description:
This hw uses varios functionalities of python using dictionaries and lists.
'''


def ltranslate(some_list,some_dict):
	"""
	replaces any occurrences of the key in a list with the key’s corresponding
	value in a dictionary.
	some_list: list
	some_dict: dictionary
	"""
	for i in range(len(some_list)):
		if some_list[i] in some_dict.keys():
			some_list[i] = some_dict[some_list[i]]
			

def word_count(fname,wdict=None):
	"""
	Read the file, using each word in it as a key in lowercase. Add
    the key to the dictionary if necessary; otherwise increment the
    count for that word. Store all words in lowercase.
	fname: string
	wdict: dictionary
	returns: dictionary
	"""
	if wdict == None:
		wdict = {}
	infile = open(fname,"r")
	for line in infile:
		line = line.split()
		for word in line:
			word = word.lower()
			if word not in wdict:
				wdict[word.lower()] = 1
			else:
				wdict[word.lower()] += 1
	return wdict


def average_wc(wdict):
	"""
	This function takes a word count dictionary and returns the
    average word count. If the dictionary is empty, it returns 0.
	wdict: dictionary
	returns: float
	"""
	if len(wdict) == 0:
		return 0
	key_count = 0
	total_count = 0 
	for key in wdict:
		key_count += 1 
		total_count += wdict[key]
	return total_count/key_count	
	
def max_wc(wdict):
	"""
	This function takes a word count dictionary and returns the
    maximum word count.
	wdict: dictionary
	returns: int
	"""
	largest = 0
	for key in wdict:
		if wdict[key] > largest:
			largest = wdict[key]
	return largest
	
def dreverse(fdict):
	"""
	This function creates and returns a reverse dictionary of an inputted 
	dictionary. Each value in the forward dictionary will be a key in the
	reverse dictionary.
	fdict: dictionary
	returns: dictionary
	"""
	rdict = {}
	for key in fdict:
		if fdict[key] not in rdict:
			rdict[fdict[key]] = []
		rdict[fdict[key]].append(key)
	return rdict

def bird_weights(ifile):
	"""
	Read the data in the file into a dictionary that contains the 
	names of the birds as keys that map to lists of weights.
	ifile: string
	returns: dictionary
	"""
	infile = open(ifile,"r")
	bdict = {}
	for line in infile:
		line = line.split(":")
		key = line[0]
		values = line[1].split()
		if key.title() not in bdict:
			bdict[key.title()] = []
		for i in range (len(values)):
			bdict[key.title()].append(float(values[i]))
	return bdict	

def median(lst_orig):
    """ 
	Returns the median of a list, without changing the list. If the
    list is empty, return None. Otherwise, the median is defined as
    the middle number of a sorted sequence of numbers if the length
    of the sequence is odd; the mean of the middle two numbers if the
    length of the sequence is even.
    lst_orig: list
    returns: int
    """
    lst = lst_orig.copy()
    if len(lst) == 0:
        return None
    lst.sort()
    if len(lst) % 2 == 0:
        med_low = lst[int(len(lst) / 2 - 1)]
        med_high = lst[int(len(lst) / 2)]
        med = (med_low + med_high) / 2
        return med
    else:
        return lst[len(lst) // 2]

def median_bird_weights(bw):
    """ 
	This function takes a bird weight dictionary and returns a new
    dictionary that maps each bird species to the median of the list
    of weights for that bird.
	bw: dictionary
    returns: dictionary        
    """
    mbw = {}
    for key in bw.keys():
        # let's use our median function!
        mbw[key] = median(bw[key])
    return mbw

	
	
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    

    

if __name__ == '__main__':
    main()
