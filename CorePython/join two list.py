list1=["a","b","c"]
list2=["1","2","3"]
list3=list1+list2
list1.append(list2)
print(list3) #ans['a', 'b', 'c', '1', '2', '3']
print(list1) #ans ['a', 'b', 'c', ['1', '2', '3']] 
