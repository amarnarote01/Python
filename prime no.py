n=int(input("Enter no"))
count=0
for i in range(2,n):
    if n%i==0:
        count=1
if count==0:
    print("Prime number")
else:
    print(" Not a Prime number")