list1=[23,45,67,23,56,78,23,89,23,23]
no=23
for i in range(0,len(list1)):
     if list1[i]==no:
        list1.pop(list1[i])
print(list1)
