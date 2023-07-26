
# Python Object Oriented Programming -

# Python is a versatile programming language that supports various programming styles, including object-oriented programming (OOP) through the use of objects and classes.

# An object is any entity that has attributes and behaviors. For example, a parrot is an object. It has

# attributes - name, age, color, etc.
# behavior - dancing, singing, etc.

# Similarly, a class is a blueprint for that object.

# ___________________________________________________________________________

# Python Objects and Classes -

# An object is simply a collection of data (variables) and methods (functions). Similarly, a class is a blueprint for that object.

# _________________________________________________________________________

# Python Classes -

# A class is considered as a blueprint of objects. We can think of the class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House is the object.

# Since many houses can be made from the same description, we can create many objects from a class.


# Define Python Class-

# We use the class keyword to create a class in Python. For example,


# class ClassName:
#     # class definition

# Note: The variables inside a class are called attributes.

# __________________________________________________________


# Python Objects -

# An object is called an instance of a class. For example, suppose Bike is a class then we can create objects like bike1, bike2, etc from the class.

# # create class
# class Bike:
#     name = ""
#     gear = 0

# # create objects of class
# bike1 = Bike()

# ________________________________________________________

# Access Class Attributes Using Objects
# We use the . notation to access the attributes of a class. For example,

# # modify the name attribute
# bike1.name = "Mountain Bike"

# # access the gear attribute
# bike1.gear
# ______________________________________________________

# Example- Python Class and Objects
# # define a class
# class Bike:
#     name = ""
#     gear = 0

# # create object of class
# bike1 = Bike()

# # access attributes and assign new values
# bike1.gear = 11
# bike1.name = "Mountain Bike"

# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

# _________________________________________________________

# # define a class
# class Employee:
#     # define an attribute
#     employee_id = 0

# # create two objects of the Employee class
# employee1 = Employee()
# employee2 = Employee()

# # access attributes using employee1
# employee1.employeeID = 1001
# print(f"Employee ID: {employee1.employeeID}")

# # access attributes using employee2
# employee2.employeeID = 1002
# print(f"Employee ID: {employee2.employeeID}")

# _________________________________________________________________________
# Constructor -

# Constructor is a special method used to create and initialize an object of a class. On the other hand, a destructor is used to destroy the object.

# 1.The constructor is executed automatically at the time of object creation.

# 2. The primary use of a constructor is to declare and initialize data member/ instance variables of a class.

# Syntax of a constructor -

# def init(self):
#     # body of the constructor

# Important Points -

# 1. def: The keyword is used to define function.

# 2. init() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.

# 3. self: The first argument self refers to the current object. I


# Note:

# For every object, the constructor will be executed only once. For example, if we create four objects, the constructor is called four times.

# In Python, every class has a constructor, but it’s not required to define it explicitly. Defining constructors in class is optional.

# Python will provide a default constructor if no constructor is defined.

# _________________________________________________________________________
# Types of Constructors -

# In Python, we have the following three types of constructors.

# 1.Default Constructor
# 2.Non-parametrized constructor
# 3.Parameterized constructor

# 1.Default Constructor -
# Python will provide a default constructor if no constructor is defined. Python adds a default constructor when we do not include the constructor in the class or forget to declare it. It does not perform any task but initializes the objects. It is an empty constructor without a body.

# 2.Non-Parametrized Constructor -
# A constructor without any arguments is called a non-parameterized constructor. This type of constructor is used to initialize each object with default values.

# 3.Parameterized Constructor -
# A constructor with defined parameters or arguments is called a parameterized constructor. We can pass different values to each object at the time of creation using a parameterized constructor.
# -----------------------------------------------------------------------------------------------------------------------------

# class Employee:
#     name="" #attributes or status or class variables
#     age=0
#     sal=0
# #how to create object
# obj =Employee()           #object creation
# obj.name="Amit"           #assign the values of class attributes
# obj.age=23
# obj.sal=45000
# print(f"{obj.name}\t{obj.age}\t{obj.sal}")
# # --------------------------------------------------
# class Employee:
#     name="" #attributes or status or class variables
#     age=0
#     sal=0
#     def get_info(self):#behavior or method or instance member function
#         self.deptno=10 #instance member variable or states
#         self.dname="sales"
#         # print(f"{self.dname}\t{self.deptno}")
#         return(self.dname,self.deptno)

# #how to create object
# obj =Employee()           #object creation
# obj1=Employee()
# obj2=Employee()
# print(obj.get_info())
# print(obj1.get_info())
# print(obj2.get_info())
# obj.name="Amit"           #assign the values of class attributes
# obj1.name="amar"          #obj1 is caller object
# obj2.name="aniket"
# obj.age=23
# obj.sal=45000
# print(f"name:{obj.name}\tage:{obj.age}\tsal:{obj.sal}")
# -------------------------------------------------------

# class Student:
#     institute_name="ITP"
#     def get_info(self,stno,sname,p1,p2,p3):
#         self.m1=p1
#         self.m2=p2
#         self.m3=p3
#         self.stno=stno
#         self.name=sname

#     def show_info(self):
#         print(f"{self.stno}\t{self.name}\t{self.m1}\t{self.m2}\t{self.m3}\t{self.total}\t{self.per}")

#     def cal_result(self):
#         self.total=self.m1+self.m2+self.m3
#         self.per=self.total/3
# obj=Student()
# obj.get_info(1,"john",45,56,67)
# obj.cal_result()
# obj.show_info()

# obj1=Student()
# obj1.get_info(2,"Amar",95,86,97)
# obj1.cal_result()
# obj1.show_info()

# obj2=Student()
# obj2.get_info(3,"Krish",56,66,87)
# obj2.cal_result()
# obj2.show_info()
# -----------------------------------------------------
# constructor-to initialize the obj state
# constructir is called when obj defined 
# only one type constructor allowed in python
# class student:
#     def __init__(self):  # non parametarise constructor
#         print("Constructor invoked")
#     def show(self):
#         print("This is show fun ")
# obj=student()
# obj1=student()
# obj2=student()
# obj.show()
# obj1.show()
# obj2.show()
# -------------------------------------------------------
# parametarise constructor
# class student:
#     def __init__(self,m,n):  # parametarise constructor
#         self.a=m 
#         self.b=n

#     def show(self):
#         print(self.a,self.b)
# obj=student(2,3)
# obj1=student(10,23)
# obj2=student(5,6)
# obj.show()
# obj1.show()
# obj2.show()
#  ------------------------------------------------------
# class Bank:
#     def __init__(self,ac,name,atype,bal):
#         self.acno=ac
#         self.name=name
#         self.acctype=atype
#         self.bal=bal
#     def withdrwawl(self):
#         self.wamt=int(input("How much amt u want to withdraw "))
#         self.bal-=self.wamt
#     def deposite(self):
#         self.damt=int(input("How much amt u want to deposite "))
#         self.bal+=self.damt
#     def show(self):
#         print(f"{self.acno}\t{self.name}\t{self.acctype}\t{self.bal}\t")

# obj1=Bank(1010,"abc","savings",50000)
# obj2=Bank(1011,"xyz","current",65000)
# obj3=Bank(1012,"lmn","savings",55000)
# obj1.withdrwawl()  
# obj1.show()
# # ----------------------------------------------------------------
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

# student_list=[]
# # add instances to list
# student_list.append(student("Amar",16))
# student_list.append(student("Hrishi",16))
# student_list.append(student("Sanket",16))
# student_list.append(student("Prashik",16))
# student_list.append(student("Suraj",16))
# for obj in student_list:

#     print(obj.name,obj.rollno)
# print(student_list) 
#  -------------------------------------------------------------
# print 5 students marksheet -stno,stname,m1,m2,m3,total,per,grade
class student:
    def __init__(self,stno,stname,m1,m2,m3):
        self.no=stno
        self.name=stname
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def result(self):
        self.total=self.m1+self.m2+self.m2
        self.per=self.total/3
        if self.per>=90:
             self.grade="A grade"
        elif self.per>=80:
            self.grade="B grade"
        elif self.per>=70:
            self.grade="C grade"
        elif self.per>=60:
            self.grade="D grade"
        elif self.per>=40:
            self.grade="E grade"
        else:
            self.grade="Fail"


# student_list=[]
# student_list.append(student(1,"Amar",55,67,85))
# student_list.append(student(2,"Hrishi",25,20,35))
# student_list.append(student(3,"Sanket",58,57,87))
# student_list.append(student(4,"Shubham",65,67,95))
# student_list.append(student(5,"Aniket",59,77,85))

# or

n=int(input("how many students record want to add"))
student_list=[student(int(input(f"Enter student id of student no{i}:-")),input("Enter student name:-"),int(input("enter Marksof m1:-")),int(input("enter Marksof m2:-")),int(input("enter Marksof m3:-"))) for i in range(1,n+1) ]


for obj in student_list:
    obj.result()
    print(obj.no,obj.name,obj.m1,obj.m2,obj.m3,obj.total,round(obj.per,2),obj.grade)