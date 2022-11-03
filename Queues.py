"""

    Queues - Data Structures very similar to lists and sequences with a difference get, into out of elements of this list 
    
    Why queue ? - when we have multiple threads running if it's is non just  main thread - You need to have a structured way of getting in data and getting out  
    
    YouTube: NeuralNine
------------------------------------------------------------------
    A QUEUE is similar to a STACK, but defines a different way to add and remover elements(FIFO)

Example code:

class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def print_queue(self):
        print(self.items)
    
s = Queue()
s.push('a')
s.push('b')
s.push('c')
s.print_queue()

s.pop()
s.print_queue()

"""

import queue


#FIFO
q = queue.Queue()

numbers = [10,20,30,40,50]
for number in numbers:
    q.put(number)

print(q.get()) #get 0 index

###############################################################

#LIFO (Stack)
q2 = queue.LifoQueue()

for number in numbers:
    q2.put(number)

print(q2.get())

###############################################################

#Priority - allows us to give every element a certain priority bu passing a tuple 

q3 = queue.PriorityQueue()

q3.put((2, "Hello World"))
q3.put((11, 99))
q3.put((5, 7.5))

while not q3.empty():
    print(q3.get())
# (2, 'Hello World')
# (5, 7.5)
# (11, 99)

###############################################################
