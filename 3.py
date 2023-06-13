#3.To print greatest of 3 nos = a=30,b=40,c=50 
a=int(input("Enter 1st no"))
b=int(input("Enter 1st no"))
c=int(input("Enter 1st no"))
if a>b and a>c:
    print(f"greatest = {a}")
elif b>c:
    print(f"greatest = {b}")
else:
    print(f"greatest = {c}")