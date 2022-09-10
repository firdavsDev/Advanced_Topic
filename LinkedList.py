"""
    A LINKED LIST is a sequence of nodes where each node stores its own data and link to the next node.
    One node links to another forming what can be thought of as linked chain:
        (data:link) --> (data:link) --> (data:link)

    The firs node is called the HEAD. and it is used as "starting point " for any iteration through the list.
    The last node must have its link pointing to None to determine the end of the list.

    Unlike STACKs and QUEUEs, you can insert and remover nodes in any position of linked list (similar to a standart list)

    Linked Lists are useful when ur data is linked.
    For example: 
        1)When u need "undo/redo" functionality, the nodes can represent the state with links to the "previous" and "next" states.
        2) A PlayLisst of music, where each clip is linked with the next one

    Linked List can also be used to "create" other DATA Structures: STACK, QUEUE, GRAPH

    Linked List Types: 
        Single Linked List: Bir tomonlama
        Circular Linked List: Aylana royhat
        DOUBLY Linked List: Ikki tomonlama royhat 


    Arrays vs Linked list
    Array = Tez oqish/qidirsh. Elementlar kamroq joy oladi. Sekin qoshish ochirish. 
    Linked List = Tez yozish/Ochirish. Xotiradan samarali foydalaniladi. Sekin qidirish, Tugun kuproq joy oladi(qiymat next_path)

"""

class Node:
    """ Node class(Tugun) """
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def add_at_front(self, data):
        """ Adding firs element"""
        self.head = Node(data, self.head)
    
    def add_at_end(self, data):
        """ Add lass Node link other Node"""
        if not self.head:
            self.head = Node(data, None)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)
    
    def print_list(self):
        n = self.head

        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()

    def get_last_node(self):
        n = self.head
        while n.next != None:
            n = n.next
        print(n.data)


# get object
l = LinkedList()
l.add_at_front(5)
l.add_at_end(8)
l.add_at_end(4)
l.add_at_end(4)
l.add_at_end(4)
l.add_at_front(9)

l.print_list()
l.get_last_node()
