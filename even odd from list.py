l=[23,34,45,56,78,90,100,33,6,5]
even_list=[]
odd_list=[]
for i in l:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)