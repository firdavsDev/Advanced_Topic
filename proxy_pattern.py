"""
    
    Proxy Pattern - Quite similar to the decorator design pattern. Basically wrapping functionality around something and this is what the PROXT does ,
    it wraps functionality around the object creation or it uses additional layer of abstraction or u could also say protection when it comes to createing,
    inctance of classes

    YouTube: NeuralNine

"""

from abc import ABCMeta,abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    """ Meta abstract class"""

    @abstractstaticmethod
    def person_method():
        """ Interface Method"""

class Person(IPerson):

    def person_method(self):
        print("I am Person!")

class ProxyPerson(IPerson):
    def __init__(self):
        self.person = Person()

    def person_method(self):
        """Wrap function"""
        print('I am proxy functionality!')
        self.person.person_method()
        
######################

p1 = Person()
p1.person_method()

######################

p2 = ProxyPerson()
p2.person_method()

######################
