class Employee:
    name="" #attributes or status or class variables
    age=0
    sal=0
#how to create object
obj =Employee()           #object creation
obj.name="Amit"           #assign the values of class attributes
obj.age=23
obj.sal=45000
print(f"{obj.name}\t{obj.age}\t{obj.sal}")
# --------------------------------------------------
class Employee:
    name="" #attributes or status or class variables
    age=0
    sal=0
    def get_info(self):#behavior or method or instance member function
        self.deptno=10 #instance member variable or states
        self.dname="sales"
        # print(f"{self.dname}\t{self.deptno}")
        return(self.dname,self.deptno)

#how to create object
obj =Employee()           #object creation
obj1=Employee()
obj2=Employee()
print(obj.get_info())
print(obj1.get_info())
print(obj2.get_info())
obj.name="Amit"           #assign the values of class attributes
obj1.name="amar"
obj2.name="aniket"
obj.age=23
obj.sal=45000
print(f"name:{obj.name}\tage:{obj.age}\tsal:{obj.sal}")
