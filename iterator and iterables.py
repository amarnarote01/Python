# What are Iterables and Iterators 

# Iterables-is an object, that one can iterate over.It generates an when passed to iter()method.
#           Iterator is an objest using __next__() method.Iterator have the __next__()method ,
#           which returns next item of the object
# list,,tuple,dictionary are iterable objects

# Iterators-is an objest using __next__() method.Iterator have the __next__()method ,
#           which returns next item of the object
# types of Iterators:-
# 1.map- to perform perticular
# list(map(function,iterable))
# square list in normal
# l=[1,2,3,4,5,6,7]
# def sq(l):
#     sq_list=[]
#     for i in l:
#         sq_list.append(i*i)
#     print(sq_list)
# sq(l)
# or using map iterator

# l1=[1,2,3,4,5,6,7]
# def sq(a):
#     return a*a
# s=list(map(sq,l1))
# print(s)
# # or
# print(list(map(lambda s:s*s,l1)))
# # reverse list
# l=["abc","xyz","lmn"]
# def rev(i):
#     return i[::-1]
# s=list(map(rev,l))
# print(s)

#>50
# #  
# l1=[56,67,89,90,23,45,50,66]
# def sq(s):
#     if s>50:
#         return s
# print(list(map(sq,l1)))

# 2.filter for condition or
# print(list(filter(fun,iterable)))
# l2=[56,67,89,90,23,45,50,66]
# print(list(filter(lambda m:m>50,l2)))
# length>4
# names=["Amol","Amit","ram","Sham","Abhishekh"]
# def vol_con(a):
#     vcount=0
#     ccount=0
#     # l=[]
#     for i in a:
#         if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
#             vcount+=1
#         else:
#             ccount+=1
#     # l.append(vcount)
#     # l.append(ccount)
#     x=vcount,ccount
#     return(x)
# print(list(map(vol_con,names)))




# 3.reduce cummulative additon or multiplication
# print(list(reduce(fun,iterable)))
# import functools
# numbers=[1,2,3,4,5,6]
# def sum(a,b):
#     return a+b
# ans=reduce(sum,numbers)
# print(ans)
# square cube
# numbers=[1,2,3,4,5,6]
# def sq_cube(a):
#     x=a*a,a*a*a
#     return x
# print(list(map(sq_cube,numbers)))

