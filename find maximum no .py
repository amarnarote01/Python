l=[23,34,45,56,78,100,33,6,5]
max=l[0]
for i in range(1,len(l)):
    if max<l[i]:
        max=l[i]
print(f"Max number = {max}")