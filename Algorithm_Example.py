"""
Berilgan ikki so'z anagram ekanligiga tekshiring.
Misol uchun:
  is_anagram("lama", "alam") => True
  is_anagram("mosh", "shom") => True
  is_anagram("non", "nok") => False
"""
from collections import Counter, defaultdict

def generate_counter(word):
    '''
        this func  generate counter for word
        Counter(word) function
    '''
    counter = defaultdict(int)
    for char in word:
        counter[char] +=1
    return counter

def is_anagram(word1: str, word2: str) -> bool:
    """
        Kodni bu yerda yozing.
    """

    #v1
    # counter1 = generate_counter(word1)
    # counter2 = generate_counter(word2)

    #v2
    # counter1 = Counter(word1)
    # counter2 = Counter(word2)

    # return counter1 == counter2

    #v3
    counter = generate_counter(word1)
    for char in word2:
        counter[char] -= 1
    return all(val==0 for val in counter.values())


# print(is_anagram("lama", "alam"))


def two_sum(nums, target:int)->bool:
    """
    Kodni bu yerda yozing.
    """
    nums_dict = {}
    for index, num in enumerate(nums):
        if target - num in nums_dict:
            return True
        nums_dict[num] = index
        print(nums_dict)
    return False
# print(two_sum([2,7,11,15], 1))


#convert_to_binary
def convert_to_binary(num:int)->str:
    """
    Kodni bu yerda yozing.
    """
    return bin(num)[2:]

#is_power_of_two
def is_power_of_two(num:int)->bool:
    """
    Kodni bu yerda yozing.
    """
    return num > 0 and (num & (num - 1)) == 0

#sum_of_odd_numbers
def sum_of_odd_numbers(num:int)->int:
    """
    Kodni bu yerda yozing.
    """
    return sum(filter(lambda x: x % 2 == 1, range(1, num + 1)))


#merge_two_arrays
def merge_two_arrays(arr1:list, arr2:list)->list:
    """
    Kodni bu yerda yozing.
    """
    return sorted(arr1 + arr2)



