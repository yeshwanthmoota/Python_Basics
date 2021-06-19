#--------------------------------------------------------------------
class Employee:
    raise_emt=1.04  # 4% raise

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return ("{} {}".format(self.first,self.last))
    def details(self):
        print(self.fullname(),"pay: ",self.pay)
    def add_raise(self):
        self.pay=round(self.pay*self.raise_emt)
#--------------------------------------------------------------------
class Developer(Employee):  # Here class Developer inherits class Employee
    raise_emt=1.10 # 10% raise

    def __init__(self, first, last, pay, prog_lang): 
        super().__init__(first,last,pay) # calling the constructor from the parent class
        # Using super() method.
        self.prog_lang=prog_lang
#--------------------------------------------------------------------
class Manager(Employee):  # Here class Developer inherits class Employee
    raise_emt=1.12 # 12% raise
 
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay) # calling the constructor from the parent class
        # Using super() method.
        if employees==None:
            self.employees=[] # created an empty list
        else:
            self.employees=employees # added a list
    def add_employees(self, *emps):
        for emp in emps:
            self.employees.append(emp)
    def remove_employees(self, *emps):
        for emp in emps:
            self.employees.remove(emp)
    def woking_emps(self):
        print("Developers working under Manager",self.fullname(),"are: ")
        for emp in self.employees:
            print("-->",emp.fullname(),"\n")
        print("------------------")
#--------------------------------------------------------------------
emp1=Employee("William", "Wonderson", 1000000)
emp2=Employee("Sam", "Smith", 1200000)

dev1=Developer("Yeshwanth", "Mootakoduru", 2000000,"Python")
dev2=Developer("Steve", "Rogers", 2200000, "C")
dev3=Developer("Bucky", "Barnes", 2000000, "C++")
dev4=Developer("Sam", "Wilson", 1800000,"Python")
dev5=Developer("Peter", "Parker", 2000000, "Java")
dev6=Developer("Thor", "Odinson", 2000000, "C")
dev7=Developer("Tony", "Stark", 3500000,"Python")
dev8=Developer("Natasha", "Romanoff", 2200000, "Ruby")
dev9=Developer("Clint", "Barton", 1800000, "C")
dev10=Developer("Bruce", "Banner", 3000000,"Python")

mgr1=Manager("Nick", "Fury", 4500000)
mgr2=Manager("Phil", "Coulson", 4000000,[dev1,dev2])
mgr3=Manager("Daisy", "Johnson", 4000000)
mgr1.add_employees(dev7,dev10)
mgr2.add_employees(dev6,dev8,dev9)
mgr3.add_employees(dev3,dev4,dev5)

mgr1.woking_emps()
mgr2.woking_emps()
mgr3.woking_emps()

dev7.details()
dev10.details()
dev2.details()
dev6.details()
mgr1.details()
emp1.details()
print("------------------")
dev7.add_raise()
dev10.add_raise()
dev2.add_raise()
dev6.add_raise()
mgr1.add_raise()
emp1.add_raise()
print("------------------")
dev7.details()
dev10.details()
dev2.details()
dev6.details()
mgr1.details()
emp1.details()

print(help(Developer)) # Check out method resolution order in this print() statement.


#--------------------------------------------------------------------