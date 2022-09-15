"""

    Composite pattern - Many class Inherence each others (Hierarchies).
    Parents + many childs 

    YouTube: NeuralNine

"""

from abc import ABCMeta, abstractstaticmethod

class IDepartment(metaclass = ABCMeta):
    """ Interface """
    @abstractstaticmethod
    def __init__(self, employees) -> None:
        """ Implement in child class """

    @abstractstaticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartment):
    
    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"Accounting Department: {self.employees} ")
    
class Development(IDepartment):
    
    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"Development Department: {self.employees} ")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees
    
    def print_department(self):
        print("Parent Department")
        print(f"Parent Employees Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number employees {self.employees}")

dept1 = Accounting(200)
dept2 = Development(100)
######################################

paretnt_dept = ParentDepartment(300)
paretnt_dept.add(dept1)
paretnt_dept.add(dept2)
paretnt_dept.print_department()

######################################