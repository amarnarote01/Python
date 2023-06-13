msg="Welcome"
str=""
for i in msg:
    if i.isupper():
       str=str+i.lower()
    else:
        str=str+i.upper()
print(str)