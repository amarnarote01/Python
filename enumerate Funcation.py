# enumerte()-used for indexing 
# syntax :- enumerate(iterable ,start=0)
# iterable-any obj that support iteration like(list,tuple,set,dictionary)
# start-default 0 .we can change start 
# ------------------------------------------------------------
# 1.list
# A=["c","Java","Python","PHP","Web"]
# B=["1 Month","2 Month","3 Month","4 Month","5 Month"]
# for index,val in enumerate(B,1):
#     print(index,val)
# ---------------------------------------------------
# 2.dict
# student={"name":"Rohit","age":45,"course":"python"}
# for key ,val in enumerate(student.items()):
#     print(key,val)
# ------------------------------------------------------
# 3.maximum no between tow list
# l1=[2,55,1,45,23]
# l2=[10,5,10,65,3]
# list=[]
# for pair in zip(l1,l2):
#     list.append(max(pair))
# print(list)
#  -----------------------------------------------------\
# 4.
# user_id=[1,2,3]
# name=["amar","sanket","hrishi"]
# surname=["narote","patil","supkar"]
# print(list(zip(user_id,name,surname)))
# print(dict(zip(user_id,zip(name,surname))))