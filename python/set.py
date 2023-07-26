# functions
# 1. add()-add an element in set
# 2.clear()-remove all elements 
# 3.copy()-copy one set to another
# 4.difference()-returns a set containaing difference between two set
# 5.union()-return set containing the union of set
# 6.update()-add from one to another set
# 7.remove()-remove perticular element
# 8.intersection()-common elements
fruits={"apple","banana","cherry"}
y={"google","microsoft","apple"}
fruits.add("orange")
print(fruits)
x=fruits.copy()
print(x)
z=y.difference(fruits)
print(z)
z=fruits.union(y)
print(z)
x.update(y)
print(x)
# z=fruits.intersection(y)
# print(z)
for i in x:
    print(i)