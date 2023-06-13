fruits = ["Apple", "Banana", "Cherry", "Mango"]
for i in fruits:
    print(i)
print("length =",len(fruits))# for length
for i in range(0,len(fruits)):
    print(i,end=" ")
#addition 
l=[1,2,3,4,5,6,7,8,9,10]
print("\n list=",l)
sum=0
for i in l:
    sum=sum+i
print("\nsum =",sum)
##addition odd even
evensum=0
oddsum=0
for i in l:
    if i%2==0:
       evensum=evensum+i
    else:
        oddsum=oddsum+i
print("evensum=",evensum)
print("oddsum=",oddsum)



