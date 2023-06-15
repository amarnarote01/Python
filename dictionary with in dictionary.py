# D={'emp1':{'name':'Bob','job':'Manager'},
#    'emp2':{'name':'kim','job':'Developer'},
#    'emp3':{'name':'sam','job':'Admin'}}
# print(D['emp1'])
# print(D['emp2'])
# print(D['emp3'])

# print(D['emp2']['job'])
# print(D['emp3']['job'])
 
# for key,val in D.items():
#     print(f"{key}={val}")

# for key,val in D.items():
#     print(f"{key}:-")
#     for k,v in val.items():
#         print(f"{k}={v}")
#     print("-------------")
# ---------------------------------------------------------

# D1={'emp1':{'name':'Bob','job':'Manager'},
#    'emp2':{'name':'kim','job':'Developer'}}
# D2={'emp2':{'name':'max','job':'Dev'},
#    'emp3':{'name':'sam','job':'Admin'}}
# D1.update(D2)
# print(D1)
# -------------------------------------------------------
D={'emp1':{'name':'Bob','job':'Manager','sal':45000},
   'emp2':{'name':'kim','job':'Developer','sal':10000},
   'emp3':{'name':'sam','job':'Admin','sal':30000},
   'emp4':{'name':'John','job':'Admin','sal':35000},
   'emp5':{'name':'Martin','job':'Manager','sal':55000},
   'emp6':{'name':'blake','job':'Developer','sal':20000}
   }
# for key,val in D.items():
#     for k,v in val.items():
#         if k=='job' and v=='Admin':
#             print(f"{key}:-{val}")
#             print("----------------")
# print("highest salary")
# max=0
# for key,val in D.items():
#     for k,v in val.items():
#         if k=='sal':
#             if max < v:
#                 max=v
# for key,val in D.items():
#     for k,v in val.items():
#         if v==max:
#             print(key,val)  
# ------------------------------------------------
# add key value pair from user 

key=input("enter key ")    
val={}
n=int(input("enter no of key value pair"))
for i in range(1,n+1):
    k=input("enter key")
    v=input("enter val")
    val.update({k:v})
D.update({key:val})
print(D)
