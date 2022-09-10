# Mutable vs Immutable | Python
**Muatable**: List, Set, Dict, CustomClass
<br>
**Imutable**: int, float, bool, str, <b>TUBLE</b>, unicode
<br>
* List & Tuple allow dublicate
<br>
* Set & Dict not allowed dublicate
<br>
* Set{} unorders
<br>
<br>

# Data structures

1) <h3>List Items</h3>
<i>
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc and last index [-1] 
</i>

Methods:
* append() (https://www.w3schools.com/python/ref_list_append.asp) ->  Adds an element at the end of the list
* clear() (https://www.w3schools.com/python/ref_list_clear.asp) ->  Removes all the elements from the list
* copy() (https://www.w3schools.com/python/ref_list_copy.asp) ->  Returns a copy of the list
* count() (https://www.w3schools.com/python/ref_list_count.asp) ->  Returns the number of elements with the specified value
* extend() (https://www.w3schools.com/python/ref_list_extend.asp) ->  Add the elements of a list (or any iterable), to the end of the current list
* index() (https://www.w3schools.com/python/ref_list_index.asp) ->  Returns the index of the first element with the specified value
* insert() (https://www.w3schools.com/python/ref_list_insert.asp) ->  Adds an element at the specified position
* pop() (https://www.w3schools.com/python/ref_list_pop.asp) ->  Removes the element at the specified position
* remove() (https://www.w3schools.com/python/ref_list_remove.asp) ->  Removes the item with the specified value
* reverse() (https://www.w3schools.com/python/ref_list_reverse.asp) ->  Reverses the order of the list
* sort() (https://www.w3schools.com/python/ref_list_sort.asp) ->  Sorts the list

<br>
<br>

2) <h3>Tuple Items</h3>
<i>
Tuples are used to store multiple items in a single variable.

Tuple items are ordered, unchangeable, and allow duplicate values.

Note: Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created. 

Tuple items are indexed, the first item has index [0], the second item has index [1] etc and last index [-1]
</i>

Methods:
* count() (https://www.w3schools.com/python/ref_tuple_count.asp) ->  Returns the number of times a specified value occurs in a tuple
* index() (https://www.w3schools.com/python/ref_tuple_index.asp) ->  Searches the tuple for a specified value and returns the position of where it was found


<br>
<br>

3) <h3>Set Items</h3>
<i>

A set is a collection which is unordered, unchangeable*, and unindexed
set items do not allow duplicate  values

Note: Set items are unchangeable, but you can remove items and add new items.
Note: Sets are unordered, so you cannot be sure in which order the items will appear.
</i>

Methods:
*add() (https://www.w3schools.com/python/ref_set_add.asp) ->  Adds an element to the set
*   clear() (https://www.w3schools.com/python/ref_set_clear.asp) ->  Removes all the elements from the set
*   copy() (https://www.w3schools.com/python/ref_set_copy.asp) ->  Returns a copy of the set 
*   difference() (https://www.w3schools.com/python/ref_set_difference.asp) ->  Returns a set containing the difference between two or more sets
*   difference_update() (https://www.w3schools.com/python/ref_set_difference_update.asp) ->  Removes the items in this set that are also included in another, specified set
*   discard() (https://www.w3schools.com/python/ref_set_discard.asp) ->  Remove the specified item
*   intersection() (https://www.w3schools.com/python/ref_set_intersection.asp) ->  Returns a set, that is the intersection of two other sets
*   intersection_update() (https://www.w3schools.com/python/ref_set_intersection_update.asp) ->  Removes the items in this set that are not present in other, specified set(s)
*   isdisjoint() (https://www.w3schools.com/python/ref_set_isdisjoint.asp) ->  Returns whether two sets have a intersection or not
*   issubset() (https://www.w3schools.com/python/ref_set_issubset.asp) ->  Returns whether another set contains this set or not
*   issuperset() (https://www.w3schools.com/python/ref_set_issuperset.asp) ->  Returns whether this set contains another set or not
*   pop() (https://www.w3schools.com/python/ref_set_pop.asp) ->  Removes an element from the set
*   remove() (https://www.w3schools.com/python/ref_set_remove.asp) ->  Removes the specified element
*   symmetric_difference() (https://www.w3schools.com/python/ref_set_symmetric_difference.asp) ->  Returns a set with the symmetric differences of two sets
*   symmetric_difference_update() (https://www.w3schools.com/python/ref_set_symmetric_difference_update.asp) ->  inserts the symmetric differences from this set and another
*   union() (https://www.w3schools.com/python/ref_set_union.asp) ->  Return a set containing the union of sets
*   update() (https://www.w3schools.com/python/ref_set_update.asp) ->  Update the set with the union of this set and others


<br>
<br>


4) <h3>Dictionary Items</h3>
<i>
    Dictionary items are ordered, changeable, and does not allow duplicates.
    Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
</i>

Methods:
* clear() (https://www.w3schools.com/python/ref_dictionary_clear.asp) ->  Removes all the elements from the dictionary
* copy() (https://www.w3schools.com/python/ref_dictionary_copy.asp) ->  Returns a copy of the dictionary
* fromkeys() (https://www.w3schools.com/python/ref_dictionary_fromkeys.asp) ->  Returns a dictionary with the specified keys and value
* get() (https://www.w3schools.com/python/ref_dictionary_get.asp) ->  Returns the value of the specified key
* items() (https://www.w3schools.com/python/ref_dictionary_items.asp) ->  Returns a list containing a tuple for each key value pair
* keys() (https://www.w3schools.com/python/ref_dictionary_keys.asp) ->  Returns a list containing the dictionary's keys
* pop() (https://www.w3schools.com/python/ref_dictionary_pop.asp) ->  Removes the element with the specified key
* popitem() (https://www.w3schools.com/python/ref_dictionary_popitem.asp) ->  Removes the last inserted key-value pair
* setdefault() (https://www.w3schools.com/python/ref_dictionary_setdefault.asp) ->  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
* update() (https://www.w3schools.com/python/ref_dictionary_update.asp) ->  Updates the dictionary with the specified key-value pairs
* values() (https://www.w3schools.com/python/ref_dictionary_values.asp) ->  Returns a list of all the values in the dictionary


