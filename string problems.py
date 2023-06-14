#upper to lower and lower to upper 
#string can't change in python so use another  

msg="Welcome"
str=""
for i in msg:
    if i.isupper():
       str=str+i.lower()
    else:
        str=str+i.upper()
print(str)