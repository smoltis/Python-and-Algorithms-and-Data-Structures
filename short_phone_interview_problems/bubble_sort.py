#!/usr/bin/env python3
"""
Bubble sort
    O(n^2)
"""

def bubble_sort(numbers):
    for index, num in enumerate(numbers):
        if num > numbers[index+1]:
            
    

if __name__ == "__main__":
    my_array = [3, 6, 2, 5, 87, 8, 3, 2, 5]
    expected = [2, 2, 3, 3, 5, 5, 6, 8, 87]
    #my_array.sort()
    assert bubble_sort(my_array) == expected
