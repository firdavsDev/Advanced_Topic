"""

Factory Disign Pattern  - if we have object and we dont know is Student or Teacher. In case define dynamaccly  Runtime help us 

YouTube: NeuralNine
"""
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    """ Meta abstract class"""

    @abstractstaticmethod
    def person_method():
        """ Interface Method"""

class Student(IPerson):
    """ Student class inherance from IPerson"""
    def __init__(self) -> None:
        self.name = "Nasic Student Name"
    
    def person_method(self):
        print("I am student")
    
class Teacher(IPerson):
    """ Teacher class inherance from IPerson"""    
    def __init__(self) -> None:
        self.name = "Basic Teacher Name"
    
    def person_method(self):
        print('I am Teacher')


class PersonFactory():
    
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
            return Teacher()
        else:
            print('Invalid Person type')
            return -1

if __name__ == "__main__":
    choice = input("What type of person do u want create? \n ")
    person = PersonFactory.build_person(choice)
    person.person_method()

