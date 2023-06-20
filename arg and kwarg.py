# *args and **kwrgs-
# 1.args -(when calling function that time pass arguments as a form of *args)
# 2.**kwargs-keyword arguments like dictionary. whwn calling function that time
#   keyword argument as a form of **kwargs
# 3.default argument-
# ------------------------------------------------------------------------
# 1.*args
# def fun(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# fun(1,2,3,4,5,6,7,8,9)
# -----------------------------------------------------
# *args with normal parameter
# def fun(n1,n2,n3,*args):
#     print(n1,n2,n3)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# fun(1,2,3,4,5,6,7,8,9)
# -----------------------------------------------------
# unpacking of args
# fun(*l)-unpack the list
# l=[1,2,3,4]
# def fun(*args):
#     for i in args:
#         print(i)
# fun(*l)
# or
# l=[1,2,3,4]
# def fun1(*args):
#     for i in args:
#         for j in i:
#           print(j)
# fun1(l)
# -----------------------------------------------------
# break -to exit or break the current loop
# continue -to continume the loop
# pass -ignore the bloch statement (if ,for ,fun)
# -----------------------------------------------------
# 1.print 1 to 10 nos on console except 5
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)
# ----------------------------------------------
#  2.**kwargs
# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs)) #type or class of kwargs ans class =dict
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")

# fun(name="amar",sub="python",marks=50,age=23,)
# ------------------------------------------------
# unpacking of kwargs
# d={"name":"amar","sub":"python","marks":50,"age":23}
# def fun(**kwargs):
#     print(kwargs)
#     print(type(kwargs)) #type or class of kwargs ans class =dict
#     for key,val in kwargs.items():
#         print(f"{key}:{val}")

# fun(**d)            #--kwargs unpack
# -------------------------------------------------
# 3.default argument
# def fun(a,b,c=100):
#     print(a+b+c)#ans 7
# fun(1,2,4)
# def fun(a,b,c=100):#c=100 is default argument
#     print(a+b+c)#ans 106
# fun(2,4)
# --------------------------------------------------
# Assignment 
#  1.Write a function that accepts s string and counts the number of upper
#    and lower case letters.
# def count(str):
#     cupper=0
#     clower=0
#     for i in str:
#         if i!=" ":
#             if i==i.upper():
#                 cupper+=1
#             if i==i.lower():
#                 clower+=1
#     print(cupper)
#     print(clower)

# str="Welcom to Itp"
# count(str)
# -----------------------------------------------------------
# 2. Write a function that takes a list and returns a new list with distinct
#     elements from the first list
# l=[1,2,3,4,5,6,7,8,9,1,3,6,10,5]
# def dictinct(l):
#     s=set(l)
#     l2=list(s)
#     print(l2)
# dictinct(l)
# 3. Write a function that takes a number as a parameter and checks whether
#    the number is prime or not
# def prime_or_not(n):
#     count=0
#     for i in range(2,n):
#         if n%i==0:
#             count=1
#     if count==0:
#         print("No is prime")
#     else:
#         print("No is not prime")
# n=int(input("Enter no"))
# prime_or_not(n)
# 4. Write a Function to create a list where the values are the squares of
#    numbers between 1 to 30(both included)
# def fun():
#     l=[]
#     for i in range(1,31):
#         l.append(i*i)
#     print(l)
# fun()