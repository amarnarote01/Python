#4. If the three sides of a triangle are entered through the keyboard,
# write a program to check whether thr triangle is valid or not.
# The triangle is valid if the sum of two sides is greater than the largest of the three sides.
a,b,c=[int(x) for x in input("Enter triangle sides :").split()]
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")