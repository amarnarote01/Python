# 1.Create two strings and concatenate both into a third string
# str1=input("enter first string ")
# str2=input("enter second string ")
# str=str1+str2
# print(str)
#------------------------------------------------------------------
# 2.Write a Python program to get the 4th element from the last element of a tuple.
# tuplex = ("a","b", "c", "d", "e", "f", "g")
# print(tuplex)
# x = tuplex[-4]
# print(x)
# ---------------------------------------------------------------------

# 3.Write a Python program to find repeated items in a tuple.
# tuple=(1,2,3,4,5,6,7,8,1,3,9,6,2,1)
# count=0
# list=[]
# for i in tuple:
#     count=tuple.count(i)
#     if count!=1:
#         list.append(i)
# print(list)
# -------------------------
# tup=(1,3,4,32,1,1,1)  
# for i in tup:
#     if tup.count(i) > 1:
#         print(i,'REPEATED')
# ---------------------------------------------------------------------------------
# 4.Write a Python program to get the smallest number from a list.
# list=[21,34,12,45,56,11,5,6,123]
# list.sort()
# print(f"smallest={list[0]}")
# -----------------------------------------------------------------------------
# 5.Write a Python program to remove duplicates from a list.
# list=[1,2,3,4,5,6,7,8,1,3,9,6,2,1]
# count=0
# for i in list:
#     count=list.count(i)
#     if count!=1:
#         list.remove(i)
# print(list)
# --------------------------------------------------------------------------

# 6.Write a Python program to find the list of words that are longer than n from a given list of words.
# list=input("enter strings saperating by space  : ").split()
# n=int(input("enter value of n "))
# list2=[]
# for i in list:
#     if (len(i)> n) :
#         list2.append(i)
# print("list of words : ",list2)
# ---------------------------------------------------------------------------------

# 7.print Fibbonacci series upto the range
#fibbonacci series upto given range
# no=int(input("Enter no"))
# a=-1
# b=1
# for i in range(0,no):
#     sum=a+b
#     print(sum,end=" ")
#     a=b
#     b=sum
# --------------------------------------------------------------------------------
# 8.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the 
# values are the square of the keys.
# list=input("enter keys by saperating space").split()
# dict={}
# for i in list:
#     dict.update({i:int(i)*int(i)})
# print(dict)
# -------------------------------------------------------------------------------
# 9.Write a Python program to sum all the items in a dictionary.
# dict = {'a': 100, 'b': 200, 'c': 300}
# list = []
# for i in dict:
#         list.append(dict[i])
# print("Sum =", sum(list))
# ----------------------------------------------------------------------------------
# 10.Write a Python program to remove a key from a dictionary
# dict={"key1":123,"key2":1234,"key4":12345}
# dict.pop("key1")
# print(dict)