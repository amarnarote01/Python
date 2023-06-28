
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
#     def __init__(self):  # defaul constructor
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
