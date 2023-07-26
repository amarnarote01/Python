# Functions --it is self contined block of program is call as function

# types:-
# 1.Without return type Without parameters(arguments)
# 2.Without return type With parameters(arguments)
# 3.With return type Without parameters(arguments)
# 4.With return type With parameters(arguments)
# ---------------------------------------------------------
# syntax:-
# 1. def function_name():      -function defination
#        body of function
# 2. function_name()           -function call
# -----------------------------------------------
# 1.Without return type Without parameters(arguments)
# def fact():
#     n=int(input("enter no"))
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f)
# fact()
# ---------------------------------------------------------
# 2.Without return type With parameters(arguments)
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f)
# n=int(input("enter no"))
# fact(n)
# ---------------------------------------------------------
# 3.With return type Without parameters(arguments)
# def fact():
#     n=int(input("enter no"))
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# print(fact())    
# # or
# # ans=fact()
# # print(ans)
# ---------------------------------------------------------
# 4.With return type With parameters(arguments)
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     return f
# n=int(input("enter no"))
# print(fact(n))
# # or
# # ans=fact(n)
# # print(ans)
# ---------------------------------------------------------
# A.reverse of list 
# 1.Without return type Without parameters(arguments)
# def rev():
#     l=[23,45,56,67,89]
#     l1=[]
#     for i in l :
#         l1.append(int(str(i)[::-1]))
#     print(l1)
# rev()
# -------------------------------------------------
# 2.Without return type With parameters(arguments)
# def rev(l):
#     l1=[]
#     for i in l :
#         l1.append(int(str(i)[::-1]))
#     print(l1)
# l=[23,45,56,67,89]
# rev(l)
# --------------------------------------------------
#  3.With return type Without parameters(arguments)
# def rev():
#     l=[23,45,56,67,89]
#     l1=[]
#     for i in l :
#         l1.append(int(str(i)[::-1]))
#     return l1
# print(rev())
# -----------------------------------------------
# 4.With return type With parameters(arguments)
# def rev(l):
#     l1=[]
#     for i in l :
#         l1.append(int(str(i)[::-1]))
#     return l1
# l=[23,45,56,67,89]
# print(rev(l))
# -------------------------------------------
# B. dicytionary
# 1.Without return type Without parameters(arguments)
# def rev():
#     l=[23,45,56,67,89]
#     rev_dict={}
#     for i in l :
#         rev_dict.update({i:int(str(i)[::-1])})
#     print(rev_dict)
# rev()
# ----------------------------------------------
# 2.With return type Without parameters(arguments)
# def rev():
#     l=[23,45,56,67,89]
#     rev_dict={}
#     for i in l :
#         rev_dict.update({i:int(str(i)[::-1])})
#     return rev_dict
# print(rev())
# ----------------------------------------------
# 3.Without return type With parameters(arguments)
# def rev(l):
#     rev_dict={}
#     for i in l :
#         rev_dict.update({i:int(str(i)[::-1])})
#     print(rev_dict)
# l=[23,45,56,67,89]
# rev(l)
# -------------------------------------------
# 4.With return type With parameters(arguments)
# def rev(l):
#     rev_dict={}
#     for i in l :
#         rev_dict.update({i:int(str(i)[::-1])})
#     return rev_dict
# l=[23,45,56,67,89]
# print(rev(l))