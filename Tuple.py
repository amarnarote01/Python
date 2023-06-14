#in tuple no append ,no insert ,no pop,no remove
#below some function
#tuple() to convert in tuple
#list() to convert in list
#dict() to convert in dictonary
tuple1=(23,34,55,55,444,55)
y=list(tuple1)
y[1]=100
tuple1=tuple(y) #ovverwrite 
print(tuple1)
#functions of tuple
#count -to count value  no of times 
#index- to chck index
#len to check length
x=tuple1.count(55)
print(x)
x=tuple1.index(55)
print("index",x)
print("length=",len(tuple1))
