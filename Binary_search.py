"""
    Linear Search = O(n)
    Binary_search = O(log2n)
    
"""

def binary_search(list, item):
    low = 0
    hight = len(list)-1

    while low <= hight:
        mid = (low+hight)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = list(range(10_000_000))

print(binary_search(my_list, 45))