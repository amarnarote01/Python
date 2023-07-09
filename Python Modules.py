# 1.User defined modules

# import importing_function as x 
# print(x.name)
# print(x.n)
# print(x.n1)
# x.fun()
# print(x.sum(2,3))

#or

# from importing_function import *
# print(name)
# print(n)
# print(n1)
# fun()
# print(sum(2,3))

# or only for perticular function

# from importing_function import fun,name
# print(name)
# fun()
# --------------------------------------------------------
# 2.predefined modules
# 1.random
# import random as r
# print(r.random())
# print("--------------------")
# print(r.randint(100,200))
# print("--------------------")

# for i in range(1,11):
#     print(r.randrange(10,50))
# print("--------------------")

# r.seed(1)

# l=["amar","hrishi","sanket","prakshik"]
# r.shuffle(l)
# print(l)
# print("--------------------")
# print(r.choice(l))
# print("--------------------")

# /--------------------------------------------------------------
# # 2.Os
# import os
# print(os.getcwd())
# os.mkdir()
# print("Directory Created")
# --------------------------
l=[1,2,3,4,5,6]
l2=[1,2,3]
n=0
for i in range(0,len(l)):
    print(l2[n],l[i])
    n+=1
    if n==3:
        n=0
