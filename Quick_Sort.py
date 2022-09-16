"""
    Quicksort = O(n*log2n)
    
"""

from random import randrange


def quickSort(arr:list) -> list:
    if len(arr)<2:
        return arr
    pivot = arr.pop(randrange(len(arr)))
    kichik = [i for i in arr if i <= pivot]
    katta = [i for i in arr if i > pivot]

    return qsort(kichik) + [pivot] + qsort(katta)