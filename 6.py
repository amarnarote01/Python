"""6.Write a java program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F"""
p=int(input("Enter marks of Physics"))
ch=int(input("Enter marks of Chemistry"))
b=int(input("Enter marks of Biology"))
m=int(input("Enter marks of Mathematics"))
c=int(input("Enter marks of Computer"))
per=((p+ch+b+m+c)/5)*100
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
elif per>=40:
    print("Grade E")
else:
    print("Grade F")
