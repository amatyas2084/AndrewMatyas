'''
Author: Andrew Matyas
Date: 1/25


Description:
<summary of this program>
'''

def sort_int_string(string):
	""" this function returns a string with the argument’s integers separated by spaces
	string: string
	"""
	new_list = string.split()
	print (new_list)
	if len(new_list) > 0:
		for i in range(len(new_list)):
			new_list[i] = int(new_list[i])
		new_list.sort()
		new_string = " "
		for item in new_list:
			new_string += str(item)+" "
		return new_string[1:-1]
	else:
		return ""
		
def dash_reverse(word):
	""" This function takes one string argument and returns a new string with 
	the same characters as in the argument but in reverse order and separated by dashes.
	word: string
	"""
	word = word[::-1]
	new_word = ""
	for char in word:
		new_word += char+"-"
	return new_word[:-1]

def xslice_replace(my_string,start,end,step,replacement):
	""" function will mimic Python’s extended slice assignment functionality for lists
	my_string: string
	start: int
	end: int
	step: int
	replacement: string
	"""
	main = list(my_string)
	replace = list(replacement)
	print(main)
	print(replace)
	main[start:end:step] = replace 
	main = "".join(main)
	return main
	
def element_ip_replace(lst_1, item, replacement=None):
    """ This list function mimics Python’s replace method for strings.
	lst_1: list
	item: string
	replacement: object
    """
    for i in range(len(lst_1)):
        if lst_1[i] == item:
            lst_1[i] = replacement


def element_nl_replace(lst_1, srch, replacement=None):
    """ This list function mimics Python’s replace method for strings. 
	lst_1: list
	srch: string
	replacement: object
    """
    nl = []
    for i in range(len(lst_1)):
        if lst_1[i] == srch:
            nl.append(replacement)
        else:
            nl.append(lst_1[i])
    return nl

def list_lt(lst_1, lst_2):
    """ This function takes two lists as arguments and returns a new list. 
	lst_1: list
	lst_2: list
    """
    if len(lst_1) is not len(lst_2):
        return None
    nl = []  # new boolean list
    for i in range(len(lst_1)):
        nl.append(lst_1[i] < lst_2[i])
    return nl


def sum_of_powers(bases, exp):
    """ This function sums exponentiated lists.
	bases: list
	exp: list
    """
    nl = []
    i = 0
    while i < len(exp): 
        total = 0        
        j = 0            
        while j < len(bases):
            total += bases[j]**exp[i]
            j += 1
        nl.append(total)
        i += 1
    return nl


def trace(m_x):
    """ This function takes one argument – a list of lists representing the 
	matrix and returns the trace of that matrix.
	m_x: matrix
    """
    i = 0
    sum_m = 0
    while i < len(m_x[0]):
        sum_m += m_x[i][i]
        i += 1
    return sum_m


def str_by_twos(string):
    """ This function takes a string argument and returns a list of each pair 
	of adjacent characters in order.  
	string: string
    """
    nl = []
    if len(string) > 1:
        for i in range(len(string) - 1):
            nl.append(string[i:i+2])  # append by twos
    return nl
		
	
