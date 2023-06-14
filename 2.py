"""2.Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Marks in Maths >=65
Marks in Phy >=55
Marks in Chem>=50
Total in all three subject >=180"""
m=int(input("Enter maths marks"))
p=int(input("Enter Phy marks"))
c=int(input("Enter Chem marks"))
t=m+p+c
if m>=65 and p>=55 and c>=50 and t>=180:
    print("Eligible for admission")
else:
    print("Not Eligible for admission")
