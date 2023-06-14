n1,n2=[int(x)for x in input("enter nos").split()]
if n1 < n2:
    for i in range (n1,n2+1):
        print(i,end=" ")
else:
    for i in range (n2,n1+1):
        print(i,end=" ")
