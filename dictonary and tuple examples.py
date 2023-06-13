"""employee={
    "empno":101,
    "ename":"soham",
    "sal":78000,
    "deptno":10,
    "job":"Manager"
}"""
#print  keys and values from employee dictionary
"""
print(employee)
for key,val in employee.items():
    print(f"{key}:{val}")"""
#print only keys from employee dictionary
"""
for key in employee.keys():
    print(key)"""
#print only values from employee dictionary
"""
for val in employee.values():
    print(val)
"""
#add new key and value pair in employee dict
"""
key,val=input("Entey Key and value ").split()
employee.update({key:val})
print(employee)"""
#delete key and value pair in dictionary
"""
key=input("enter key you want to delete ")
employee.pop(key)
print(employee)"""
#enter eny and print val
"""
key=(input("enter key "))
if key in employee.keys(): #or employee:
    print(employee[key]) #or print(employee.get(key))
else:
    print("key not available")"""
#convet dictionary to list
"""
marks={ "a":56,"b":78,"c":90,"d":23,"e":45,"f":100,"g":67}
list=[]
for val in marks.values():
    if val >= 50:
        list.append(val)
print(list)"""
#cube dictionary 
"""list1=[3,4,5,6,7,8,9,10]
cube_dict={}
for i in range(0,len(list1)):
    x=list1[i]*list1[i]*list1[i]
    cube_dict.update({list1[i]:x})
print(cube_dict)"""
#the join()method takes all items in an iterable 
# and joins them into one string
"""
l1=["john","blake","scott","martin"]
names = " ".join(l1)
print(names)
"""
"""
d={"name":"abc","age":"23","marks":"56"}
names = " ".join(d)    #print only keys as default
print(names)
names = " ".join(d.values())    #only for string values
print(names)"""
#remove special symbols and char from string 
#try yourself
"""
message="ffdgjdk645768=-.jggsyufu123@"
token="sfdh"
"""
#tuple to string using join 
"""
t=(34,4,5,67,89,90)

names="".join(str(t))
print(names) #ans (34, 4, 5, 67, 89, 90)
"""
#
msg="Itp is best training institute"
# x=msg.split()
# itp=[]
# for i in x:
#     itp.append(i)
#or
itp=[msg.split()]
print(itp)