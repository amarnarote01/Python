
# 1.Append new string in the middle of a given string

# for Ex. s1 = "Ault"
#         s2 = "Kelly"

# output - AuKellylt
# ----------------------------------------------------------------
# s1="ault"
# s2="kelly"
# l=[]
# for i in range(0,len(s1)//2):
#     l.append(s1[i])
# for i in s2:
#     l.append(i)
# for i in range(len(s1)//2,len(s1)):
#     l.append(s1[i])
# s="".join(l)
# print(s)
# ____________________________________________________________________________

# 2.Arrange string characters such that lowercase letters should come first.

# Given:
# str1 = PyNaTive

# Expected Output:
# yaivePNT
# ---------------------------------------
# str1="PyNative"
# l=[]
# for i in str1:
#     if i.islower():
#         l.append(i)
# for i in str1:
#     if i.isupper():
#         l.append(i)
# s="".join(l)
# print(s)

# _____________________________________________________________________________
# 3.Convert two lists into a dictionary.

# Ex. keys = ['Ten', 'Twenty', 'Thirty']
#     values = [10, 20, 30]

# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# --------------------------------------------------
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict={}
# for i in range(3):
#     dict.update({keys[i]:values[i]})
# print(dict)

# ____________________________________________________________________________

# 4.Print the value of key ‘history’ from the below dict

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# Expected output:

# 80
# # ------------------------------------------------
# sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
# print(sampleDict["class"]["student"]["marks"]["history"])
#____________________________________________________________________________
# 5.Remove items from the set at once

# Remove items - 10,20,30

# Given:

# set1 = {10, 20, 30, 40, 50}

# Expected output:

# {40, 50}
# ----------------------------------------------
# set1 = {10, 20, 30, 40, 50}
# set1.remove(10)
# set1.remove(20)
# set1.remove(30)
# print(set1)
# ____________________________________________________________________________

# 6.Update set1 by adding items from set2, except common items

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {70, 10, 20, 60}
# # -----------------------------------------------

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# mylist=[]
# for i in set1:
#     if i  not in set2:
#         mylist.append(i)
# for i in set2:
#     if i  not in set1:
#         mylist.append(i)
# print(set(mylist))

# ___________________________________________________________________________
# 7.Swap two tuples in Python
# Given:

# tuple1 = (11, 22)
# tuple2 = (99, 88)
# x=tuple1
# tuple1=tuple2
# tuple2=x
# print(tuple1)
# print(tuple2)


# ________________________________________________________________________
# 8.Remove special symbols / punctuation from a string

# Given:
# str1 = "/*Jon is @developer & musician"

# Expected Output:

# # "Jon is developer musician"
# str1 = "/*Jon is @developer & musician"
# str=[]
# for i in str1:
#     if "a"<=i<="z" or "A"<=i<="Z" or i==" ":
#         str+=i
# s="".join(str)
# print(s)

# __________________________________________________________________________

# 9.Removal all characters from a string except integers

# Given:

# str1 = 'I am 25 years and 10 months old'

# # Expected Output:

# 2510
# --------------------------

# str1 = 'I am 25 years and 10 months old'
# str=[]
# for i in str1:
#     if "0"<=i<="9":
#         str+=i
# s="".join(str)
# print(s)
# ___________________________________________________________________________