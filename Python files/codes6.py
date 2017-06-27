'''
Author: Andrew Matyas
Date: 3/30


Description: runs various programs dealing with arrays.
'''
import numpy as np


def reverse(arr):
    """ This functions returns a reverse of a given array

    Args:
        arr -- (Array) to be reverse
    returns:
        reverse of arr
    """
    return arr[::-1]


def odd_even_mask(arr):
    """ This function takes an array as an argument and returns a new
    array of the same length that has zeros corresponding to even numbers
    in the argument and ones corresponding to odd arguments.

    Args:
        arr -- (Array) array to be copied and manipulated

    return:
        copy of arr, with the even indexes replaced with 0's and the
        odd's replaced with 1's
    """
    back = np.zeros(len(arr), dtype=np.int)
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            back[i] = 1
    return back


def cycle(arr, num):
    """ This function takes an array as its first argument and an integer
    n as its second. It returns a new array that has the same elements n
    places to the right. When an element shifts of the right end of the
    array, it wraps around to position 0.

    Args:
        arr -- (Array) to be shifted
        num -- (int) "shift by" value

    return:
        a new array shifted by the given integer
    """
    shift = np.zeros(len(arr))
    for i in range(len(arr)):
        shift[(i + num) % len(arr)] = arr[i]
    return shift


def double(arr):
    """ this function takes an array as an argument and returns a new
    array that has each element doubled.

    Args:
        arr -- (Array) an array to be doubled

    returns:
        new array that is a double of the argument
    """
    double = np.empty_like(arr)
    for i in range(len(arr)):
        double[i] = 2 * arr[i]
    return double


def double_ip(arr):
    """ This function takes an array as an argument doubles each element
    in place.

    Args:
        arr -- (Array) an array to be doubled

    returns:
        n/a
    """
    for i in range(len(arr)):
        arr[i] = 2 * arr[i]


def square_evens(arr):
    """ This function takes an array as an argument replaces each even
    element with its square.

    Args:
        arr -- (Array) and array with some elements to be doubled

    returns:
        n/a
    """
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] *= arr[i]


def binary_search(key, arr):
    """ This function searches for a key in an array, returns an index
    if the key is found, else it returns -1. Duplicate instances of the
    key are unimportant.

    Args:
        key -- (int) search array for this
        arr -- (Array) to be searched
    """
    low = 0
    high = len(arr)
    while low <= high:
        index = int((low + high) / 2)
        if index == high:
            break
        if arr[index] == key:
            return index
        elif arr[index] > key:
            high = index
        else:
            low = index + 1
    return -1


def insert(arr, index, value, overwrite):
    """ Assume that index is a nonnegative integer. If it is too large,
    raise an IndexError. If overwrite is False, shift all values from
    index and higher one spot to the right, eliminating the last item.
    Set the element at position index to value.

    Args:
        arr -- (Arr) an array to be editted
        index -- (int) nonnegative, pivot point
        value -- (int) index to be replaced
        overwrite -- (Boolean) to shift or replace
    """
    if index > len(arr):
        raise IndexError
    if not overwrite:
        for i in range(len(arr) - 2, index - 1, -1):
            temp = arr[i]
            arr[i + 1] = arr[i]
    arr[index] = value


def swap(arr, ind1, ind2):
    """ This function takes three variables, an array and two integers.
    Swap the values at the indices given by the two integers. Don't do
    any error checking.

    Args:
        arr -- (Array) in which indexes are swapped
        ind1 -- (int) to swap with ind2
        ind2 -- (int) to swap with ind1

    returns:
        n/a
    """
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def add_arrays(arr1, arr2):
    """ This function takes two array arguments. Return a new array that
    is the length of the longer of the two arguments. The element at each
    position of the new array is the sum of the elements in the
    corresponding positions in the two arguments. If one array is longer,
    fill the remaining positions in the new array with the values in the
    corresponding positions in the longer array.

    Args:
        arr1 -- (Array) to add
        arr2 -- (Array) to add

    returns:
        a new array of sums, plus overflow
    """
    if len(arr1) > len(arr2):
        new_arr = np.array(arr1, copy=True, dtype=float)
        for i in range(len(arr2)):
            new_arr[i] += arr2[i]
    else:
        new_arr = np.array(arr2, copy=True, dtype=float)
        for i in range(len(arr1)):
            new_arr[i] += arr1[i]
    return new_arr



def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
if __name__ == '__main__':
    main()