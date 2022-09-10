"""
    Stack is a simple data structure thats adds and 
    removes elements in a particular order.

    Every time an element is added, it goes on the "TOP" of stack.

    it is LIFO *Last In, First Out"

    push = add elemtent
    pop = remove element
    isEmpty
    isFull
    Peel = top 
"""

class Stack:
    
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()
