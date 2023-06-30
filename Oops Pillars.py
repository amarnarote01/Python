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
class emp:
    def set_name(self,name):#setter
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_sal(self,sal):
        self.sal=sal
    def get_name(self): #getter
        return self.name
    def get_age(self):
        return self.age
    def get_sal(self):
        return self.sal

obj=emp()
obj.set_name("abc")
obj.set_age(25)
obj.set_sal(45000)
print(obj.get_name())
print(obj.get_age())
print(obj.get_sal())