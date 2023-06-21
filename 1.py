# # This program prints Hello, world!

# print('Hello, world!')

# """1. To ask user that how many days in a leap year. 

# a. if user will get correct ans -
#       then print "You have cleared the first level" and ask again another que "What month has an extra day in leap year?" if user will get correct answer then display message "Congratulations !!You have cleared the test" otherwise "You have failed the test".

# b.otherwise print following msg-

#       "Your input is wrong, please try again."""
 

# x=int(input("how many days in a leap year? "))
# if x==366:
#     print("You have cleared the first level")
#     y=input("What month has an extra day in leap year? ")
#     if y=="feb" :
#         print("Congratulations !!You have cleared the test")
#     else:
#         print("You have failed the test")
# else :
#     print("Your input is wrong, please try again.")

# # ------------------------------------------------------------------------------

# """2.Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
# Marks in Maths >=65
# Marks in Phy >=55
# Marks in Chem>=50
# Total in all three subject >=180"""
# m=int(input("Enter maths marks"))
# p=int(input("Enter Phy marks"))
# c=int(input("Enter Chem marks"))
# t=m+p+c
# if m>=65 and p>=55 and c>=50 and t>=180:
#     print("Eligible for admission")
# else:
#     print("Not Eligible for admission")

# #3.To print greatest of 3 nos = a=30,b=40,c=50 
# a=int(input("Enter 1st no"))
# b=int(input("Enter 1st no"))
# c=int(input("Enter 1st no"))
# if a>b and a>c:
#     print(f"greatest = {a}")
# elif b>c:
#     print(f"greatest = {b}")
# else:
#     print(f"greatest = {c}")
# # ------------------------------------------------------------------------------

# #4. If the three sides of a triangle are entered through the keyboard,
# # write a program to check whether thr triangle is valid or not.
# # The triangle is valid if the sum of two sides is greater than the largest of the three sides.
# a,b,c=[int (x) for x in input("enter 3 values").split()]
# if a>b and a>c and b+c>a:
#     print("Traingle is valid")
# elif b>c and a+c>b:
#     print("Triangle is valid")
# elif b+a>c:
#     print("Triangle is valid")
# else:
#     print("Triangle is invalid")
# # ------------------------------------------------------------------------------
# #5. Write a java program to input any alphabet and check whether it is vowel or consonant.
# ch=input("Enter alphabet")
# if ch=='a' or ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or  ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
#     print("This is vowel")
# else :
#     print("This is not a vowel")
# # ------------------------------------------------------------------------------
# """6.Write a java program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F"""
# p=int(input("Enter marks of Physics"))
# ch=int(input("Enter marks of Chemistry"))
# b=int(input("Enter marks of Biology"))
# m=int(input("Enter marks of Mathematics"))
# c=int(input("Enter marks of Computer"))
# per=((p+ch+b+m+c)/5)*100
# if per>=90:
#     print("Grade A")
# elif per>=80:
#     print("Grade B")
# elif per>=70:
#     print("Grade C")
# elif per>=60:
#     print("Grade D")
# elif per>=40:
#     print("Grade E")
# else:
#     print("Grade F")
# # -----------------------------------------------------
# #7. - Design
# """Half
# Faulty
# Calculator
# 45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4
# Design a calculator which will correctly solve all the problems except
# # the following ones:
# # 45 * 3 = 555, 56+9 = 77, 56/6 = 4  ex  - 56/6
# # Your program should take operator  and the two numbers as input from the user
# # and then return the result"""
# a=int(input("Enter first no. "))
# b=int(input("Enter second no. "))
# operator=input("Enter operator + - * / % ")
# if a==56 and b==9 and operator=='+':
#     print("77")
# elif a==45 and b==3 and operator=='*':
#     print("555")
# elif a==56 and b==6 and operator=='/':
#     print("4")
# elif operator=='+':
#     print(a+b)
# elif operator == '-':
#     print(a-b)
# elif operator=='*':
#     print(a*b)
# elif operator=='/':
#     print(a/b)
# elif operator == '%':
#     print(a%b)
