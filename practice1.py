#addition of digits in given number
# n= input("Enter no")
# sum=0
# for i in n:
#     sum+= int(i)
# print(f"Digit adddition ={sum}")
#------------------------------------------------
#addition of digits in given number
# n= input("Enter no")
# sumeven=0
# sumodd=0
# for i in n:
#     if int(i)%2==0:
#         sumeven =sumeven + int(i)
#     else:
#         sumodd = sumodd + int(i)
# print(f"adddition of even digit  ={sumeven} adddition of odd digit  ={sumodd}")

#----------------------------------------------------

# reverse of no
# n= input("Enter no")
# print(n[::-1])
#-------------------------------------
#fibbonacci series upto given range
# no=int(input("Enter no"))
# a=-1
# b=1
# for i in range(0,no):
#     sum=a+b
#     print(sum,end=" ")
#     a=b
#     b=sum
#------------------------
#print number upto the range 
# if the no is divisible by 
# n/3==Fizz
#n/5==Bizz
#n/3 and n/5==Fizz Bizz

# n=int(input("enterno"))
# n=n+1
# for i in range(1,n):
#     if i%3==0 and i%5==0:
#         print(f"{i} FizzBizz")
#     elif i%3==0:
#         print(f"{i} Fizz")
#     elif i%5==0:
#         print(f"{i} Bizz")
#     else:
#         print(i)
#------------------------------------------
#create capital dictionary 
# str="Welcome to  itp"
# capital={}
# for i in str:
#     capital.update({i:i.upper()})
# print(capital)
#---------------------------------
# Ascii no operation
#0-9=48-57
#A-Z=65-90
#a-z=97-122
# ord()-for char to ascii Value
# chr()- for value to char
#----------------------------------

#1Enter the string from user for ex str="wel45tyftr&&4asQ"
#and print count digits ,uppercase letter ,lower case letters and special symbols

# str="wel45tyftr&&4asQ"
# digitcount=0
# uppercount=0
# lowercount=0
# specialcount=0
# for i in str:
#     i=ord(i)
#     if i>=65 and i<=90:
#         uppercount+=1
#     elif i>=97 and i<=122:
#         lowercount+=1
#     elif i>=47 and i<=56:
#         digitcount+=1
#     else:
#         specialcount+=1
# print(f"digit vount={digitcount} \n uppercase count={uppercount}\n lowercase count={lowercount}\nspecial char count={specialcount}")

#---------------------------------------------

#2 Enter the any number from user and print number in word like 
#number=123-ans-one two three
# no= input("enter no")
# for i in no:
#     if i=="1":
#         print("one",end=" ")
#     elif i=="2":
#         print("two",end=" ")
#     elif i=="3":
#         print("three",end=" ") 
#     elif i=="4":
#         print("four",end=" ") 
#     elif i=="5":
#         print("five",end=" ") 
#     elif i=="6":
#         print("six",end=" ") 
#     elif i=="7":
#         print("seven",end=" ") 
#     elif i=="8":
#         print("eight",end=" ") 
#     elif i=="9":
#         print("nine",end=" ")
#     else:
#         print("zero",end=" ")

#---------------------------------

#3enter the string from user for ex. str="welc234tyu%^"

# and remove special symbols and numbers in given strig
# str=input("enter string") 
# for i in str:
#     i=ord(i)
#     if i>=65 and i<=90:
#         print(chr(i),end="")
#     elif i>=97 and i<=122:
#         print(chr(i),end="")
#     elif i>=47 and i<=56:
#         continue
#     else:
#         continue
#        or 

# str=input("enter string")
# list1=list(str)
# list2=[]
# for i in str:
#     if (i>="a" and i<="z") or (i>="A" and i<="Z"):
#         list2.append(i)
# print(list2)
# str1="".join(list2)
# print(str1)
#---------------------------------------------------
#note
# lstrip- remove spaces from left side 
# rstrip- remove spaces from rigth side
# strip- remover spaces from both side 
#---------------------------------------------------

# 4. '''Create cube dictionary from existing list'''

# list ={1,2,3,4,5,6,7,8,9,10}
# cube_dict={}
# for i in list:
#     cube_dict.update({i:i*i*i})
# print(cube_dict)

#----------------------------------------------------------------

# 5. '''print the length of number without len() function'''


# n=input("enter no ")
# count=0
# for i  in n:
#     count+=1
# print("length=",count)
#----------------------------------------------------
#1. change the specific element in given tuple
# t=(34,5,67,88,90,33,12)
# index=int(input("which value u want to change specify the index number"))
# value=int(input("enter value"))

# l=list(t)
# l[index]=value
# t=tuple(l)
# print(t)

#or

# list=[]
# list2=[]
# x=t
# list=t
# print(list)
# for i in range(0,len(list)):
#     if i==index:
#         list2.append(value)
#     else:
#         list2.append(list[i])
# print(list2)
# y=(list2)
# tuple=y
# print(tuple)

#---------------------------------------------
#conver tuple to dictionary
# t=(34,5,67,88,90,33,12)
# dict={}
# for i in range(0,len(t)):
#     dict.update({str(i):t[i]})
# print(dict)
#----------------------------------------------
#creat square list from tuple
# t=(34,5,67,88,90,33,12)
# square=[]
# for i in t:
#     square.append(i*i)
# print(square)
#------------------------------------------------------
#upper to lower and lower to upper 
#string can't change in python so use another  

# msg="Welcome"
# str=""
# for i in msg:
#     if i.isupper():
#        str=str+i.lower()
#     else:
#         str=str+i.upper()
# print(str)
# --------------------------------------------
# n1,n2=[int(x)for x in input("enter nos").split()]
# if n1 < n2:
#     for i in range (n1,n2+1):
#         print(i,end=" ")
# else:
#     for i in range (n2,n1+1):
#         print(i,end=" ")
# -------------------------------
# only duplicate values
# l1=[1,2,3,4,5,6,2,3,8,9,5,5]
# l2=[]
# for i in l1:
#     if l1.count(i)>1:
#         if i not in l2:
#             l2.append(i)
# print(l2)
# -----------------------------------------
# to remove all extra duplicate elements form list and create a new list of that element   
# l1=[1,2,3,4,5,6,2,3,2,3,1,1,1,1,2,8,9,2,1,2,3]
# l2=l1
# l3=[]
# l4=[]
# for i in l2:
#     if l2.count(i)>1:
#         # print(i,l2.count(i))
#         l3.append(i)
#         if i not in l4:
#             l4.append(i)
#     else:
#         l4.append(i)
# print(l4)
# print(l3)
# # ------------------------------------------