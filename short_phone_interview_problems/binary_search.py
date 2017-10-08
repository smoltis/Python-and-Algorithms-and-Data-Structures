#!/usr/bin/env python

__author__ = "bt3"

def binary_search(in_in_array, value):   
    last, first = len(in_array), 0
    
    while first < last:
        mid = (last - first)//2
        item = in_array[mid]
        
        if item == value:
            return True
        
        elif item < value:
            last = mid
        
        else:
            first = mid 
    
    return False

def binary_search_rec(in_array, value, first=0, last=None):
    last = last or len(in_array)
    if len(in_array[first:last]) < 1:
        return False
    
    mid = (last - first)//2
    if in_array[mid] == value:
        return True
    elif in_array[mid] < value:
        return binary_search_rec(in_array, value, first=first, last=mid)
    else:
        return binary_search_rec(in_array, value, first=mid, last=last)

    
if __name__ == '__main__':    
    in_array = [3, 4, 6, 7, 10, 11, 34, 67, 84]
    value = 6
    assert(binary_search(in_array, value) == True)   
    assert(binary_search_rec(in_array, value) == True)  
    value = 8
    assert(binary_search(in_array, value) == False)
    assert(binary_search_rec(in_array, value) == False)  
    in_array = [8]
    assert(binary_search(in_array, value) == True)
    assert(binary_search_rec(in_array, value) == True)  
    in_array = []
    assert(binary_search(in_array, value) == False)
    assert(binary_search_rec(in_array, value) == False)  