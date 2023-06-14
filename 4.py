#4. If the three sides of a triangle are entered through the keyboard,
# write a program to check whether thr triangle is valid or not.
# The triangle is valid if the sum of two sides is greater than the largest of the three sides.
a,b,c=[int (x) for x in input("enter 3 values").split()]
if a>b and a>c and b+c>a:
    print("Traingle is valid")
elif b>c and a+c>b:
    print("Triangle is valid")
elif b+a>c:
    print("Triangle is valid")
else:
    print("Triangle is invalid")