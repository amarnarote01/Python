#  Opps pillars:
# 1.Encapsulation
# 2.Polymorphism
# 3.Inheritance
# 4.Data Abstraction
# ----------------------------------------------------------
# 1)Encapsulation - Bundling the data and methods within a single unit. Ex- when creating a class, you are implementing encapsulation.
# means binding all the data members(instance variable ) and methods into single unit OR medicine Capsule.
# We can hide data in encapsulation
# Access modifier: limit access to the variable and methods of a class.
#     1)Public Member:Accessible anywhere from outside of class.(no _(underscore))
#     2)Protected Member: Accessible within the class and its subclass.(_(single underscore))
#     3)Private Member: Accessible with the class.(__(double underscore))
# # -----------------------------------------------------------------------------
# class emp:
#     def __init__(self,name,sal,deptno):
#         self.name=name       #public
#         self._sal=sal        #protected
#         self.__deptno=deptno #private
#     # def show_dept(self):
#     #     print(self.__deptno)

# obj=emp("abc",25500,101)
# print(obj.name)
# print(obj._sal)
# # obj.show_dept()
# # Name Mangling
# print(obj._emp__deptno) #name mangling-to access private variaables
# ======================================================================================
# getters and setters
# class emp:
#     def set_name(self,name):#setter
#         self.name=name
#     def set_age(self,age):
#         self.age=age
#     def set_sal(self,sal):
#         self.sal=sal
#     def get_name(self): #getter
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_sal(self):
#         return self.sal

# obj=emp()
# obj.set_name("abc")
# obj.set_age(25)
# obj.set_sal(45000)
# print(obj.get_name())
# print(obj.get_age())
# print(obj.get_sal())

# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# 3.Inheritance
# 3.1 single Inheritance
# 3.2 multi Inheritance
# 3.3 Hierarchical inheritance
# 3.4 Multiple inheritance
# 3.5 Hybrid inheritance
# ------------------------------------------------------------------------------------------
# using parametrised constructor
# class Bank:
#     def __init__(self,name,acno,bal,atype):
#         self.cust_name=name
#         self.acno=acno
#         self.bal=bal
#         self.actype=atype
# class customer(Bank):
#     cust_add="pune"
#     def show_info(self):
#         print(self.cust_name,self.acno,self.bal,self.actype,customer.cust_add)

# c=customer("john",12231,50000,"savings")
# c.show_info()


# -----------------------------------------------------------------------------------------
# using parametrised function
# class bank:
#     def cust_info(self,name,accno,bal,acctype):# function
#         self.custname=name        
#         self.accno=accno
#         self.bal = bal
#         self.acctype=acctype
# class customer(bank):
#     cust_add="pune"
#     def show_cust_info(self):        
#         print(f"{self.custname} {self.accno} {self.bal} {self.acctype}")
# c = customer()
# c.cust_info("suraj",2018208888,50000,"saving")
# c.show_cust_info()
# ------------------------------------------------------------------------
# 2)Multilevel Inheritance:
# from class A -> class B -> class C

# class A:
#
#     def get_a(self, a):
#         self.a = a
#         return self.a
#
#
# class B(A):
#
#     def get_b(self, b):
#         self.b = b
#
#
# class C(B):
#     c = 3
#
#     def mul(self):
#         self.result = self.get_a(2) * self.b * C.c
#         return self.result
#
#
# obj = C()
# obj.get_b(4)
# print(obj.mul())
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Default constructor calling using super():
# class A:
#     def init(self):
#         print("A Default Constructor called!!!")
#
#
# class B(A):
#     def init(self):
#         # super().init()  # If super is not present in child class then it will not call the parent constructors default constructor.
#         print("B Default Constructor called!!!")
#
#
# class C(B):
#     def init(self):
#         super().init()  # If super is present in child class then it will call the parent constructors default constructor.
#         print("C Default Constructor called!!!")
#
#
# obj = C()
# -----------------------------------------------------------------------------------------------------------------------------------------------
# Using Parameterized constructor:
# class A:
#     def init(self, a, b):
#         self.a = a
#         self.b = b
#         print(f"class_A={a}, class_A={b}")
#
#
# class B(A):
#     def init(self, a, b):
#         # super().init(a,b) # if super is not present in child class then parameterized constructor will not be called of parent class.
#         self.a = a
#         self.b = b
#         print(f"class_B={a}, class_B={b}")
#
#
# class C(B):
#     def init(self, a, b):
#         super().init(a, b)  # if super is present in child class then parameterized constructor will be called of parent class.
#         self.a = a
#         self.b = b
#         print(f"class_C={a}, class_C={b}")
#
#
# obj = C(10, 20)
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 3)Multiple Inheritance:
# class subject_marks:  # m1,m2,m3,m4
#     def get_marks(self, m1, m2, m3, m4):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#
#
# class other_activity:  # sport,music,yoga
#     def get_other_act(self, sport, music, yoga):
#         self.sport = sport
#         self.music = music
#         self.yoga = yoga
#
#
# class student(subject_marks, other_activity):
#     def show_res(self):
#         self.result = self.m1 + self.m2 + self.m3 + self.m4 + self.sport + self.music + self.yoga
#         self.per = self.result / 7
#         print(f"Total of all marks={self.result} & Percentage ={self.per}")
#
#
# obj = student()
# obj.get_marks(10, 20, 30, 40)
# obj.get_other_act(50, 60, 70)
# obj.show_res()
# ------------------------------------------------------------------------------------------------------------------------------------ 
class Animal():
    name=""
    def speak(self):
        print("animal")
class Dog(Animal):
    def speak(self):
        Dog.name="Dog"
        print(Dog.name)
        print("Bark")
class Cat(Animal):
    def speak(self):
        Cat.name="Cat"
        print(Cat.name)
        print("meow")
class Goat(Animal):
    def speak(self):
        Goat.name="Goat"
        print(Goat.name)
        print("meah")
obj1=Dog()
obj2=Cat()
obj3=Goat()
obj1.speak()
obj2.speak()
obj3.speak()