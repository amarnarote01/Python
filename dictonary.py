student={"name":"Rohit","age":45,"course":"python"}
print(student)
#functions
#1 clear-to remove all elements
#2 copy -to copy  to another dict
#3 fromkeys_returns dictonary with specified key and values
#4 get- value
#5 items-key and value
#6 keys-only keys
#7 pop-remover element with specifide key
#8 popitem()-removes last key and value
#9 update-add new key an value pair  
#10 values -return all values 
#11 join-
#student.clear()
#print(student)
new_dict=student.copy()
print(new_dict)
x=('key1','key2','key3')
y=100
this_dict=dict.fromkeys(x,y)
print(this_dict)
print(student.get("name")) # or print(student["name"])
print(student.items())
print(student.keys())
student.pop("age")
print(student)
student.popitem()
print(student)
student.update({"marks":35})
print(student)
x=student.values()
print(x)