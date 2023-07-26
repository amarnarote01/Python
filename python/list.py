#list 
# There are four collection data types in the python programming lang:
# 1.List[]--is a collection which is ordered and changeable(MUTABLE).Allows duplicate members.
# 2.Tuple()--is a collection which is ordered and unchangeable(IMMUTABLE).Allows duplicate members.
# 3.Set--is a collection which is ordered and unindexed.No duplicate members allowed.
# 4.Dictionary{}--is a collection which is unordered and changeable(MUTABLE),indexed.
# No duplicate members(key) but values can be duplicate.It is key:value pair structure
# -----------------------------------------------------------------------------------------------------------------
# 1.List:
mixed_list =[1,2,3,4,True,"welcome",'t'] #true is bullian value
print(mixed_list[4])
print(mixed_list[2:])#start from 2 to last  index
print(mixed_list[:6])#start from 0 to 5th index

fruits = ["Apple", "Banana", "Cherry", "Mango"]
print(fruits[2])
print(fruits[1])
fruits[3] = "Kiwi"
print(fruits)
print(fruits[::-1])  # reverse the list
print(fruits[-1])
print(fruits[0:2])  # slicing of list
for x in fruits:
    print(x, end=" ") # for loop for printing list elements in single line use end=" "