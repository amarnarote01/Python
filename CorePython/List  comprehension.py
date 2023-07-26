# 1.
# square_list=[]
# for i in range(1,11):
#     square_list.append(i*i)
# print(square_list)
# # list comprehension
# # list_name=[expression loop]
# square_list=[i*i for i in range(1,11)]
# print(square_list)
# ------------------------------------------------
# 2.
# l=["john","martin","scott","smith"]
# l2=[i[0] for i in l ]
# print(l2)
# ------------------------------------------
# 3.for if else
# syntax
# for if
# list_name=[expression cond for loop if]
# for if else
# list_name=[expression if else cond for loop]
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_list=[i for i in numbers if i%2==0]
# odd_list=[i for i in numbers if i%2!=0]
# print(even_list)
# print(odd_list)
# ---------------------------
# 4.
# sq_cube_list=[i*i if i%2==0 else i*i*i for i in numbers]
# print(sq_cube_list)
# # or 
# sq_list=[]
# cube_list=[]
# [sq_list.append(i*i)if i%2==0 else cube_list.append(i*i*i) for i in numbers]
# print(sq_list)
# print(cube_list)
# -----------------------------------
# 5.
# names=["john","martin","scott","smith"]
# rev_list=[i[::-1] for i in names]
# print(rev_list)
# --------------------------
# 6.
# names=["john","martin","scott","smith","mom","sos","bob"]
# pal_list=[]
# rev_list=[]
# [pal_list.append(i[::-1]) if i==i[::-1] else rev_list.append(i[::-1]) for i in names]
# print(pal_list)
# print(rev_list)
# ---------------------------------
# 7.nested loops
# syntax:-
# list_name=[[expression for loop] for loop]
#  expected output n_list=[[1,2,3],[1,2,3],[1,2,3]]
# nested_list=[[i for i in range(1,4)]for j in range(3)]
# print(nested_list)
# ------------------------------------
# assignment
# 1.write a list comprehension that builds a list contrining only the names with at least 8 characters
# list=["amar","shantanu","shrikant","sanket","hrishikesh","vishal"]
# names=[i for i in list if len(i)>=8]
# print(names)
# --------------------------------------------
# 2.add % in front and end of every single word in a given string for ex
#  "Harry is good boy"--o/p-"%Harry% %is% %good% %boy%"
# msg="Harry is good boy"
# l=["%"+i+"%" for i in msg.split() ]
# x=" ".join(l)
# print(x)
# ---------------------------------------------
# 3. Remove all odd numbars from list using lc
# numbers=[1,2,3,4,5,6,7,8,9,10]
# x=numbers
# [numbers.remove(i) for i in x if i%2!=0]
# print(numbers)
# ---------------------------------------------
# 4.find the numbers from 1-100 that are divisible by 7 using lc
# list=[i for i in range(1,100) if i%7==0]
# print(list)
# ---------------------------------------------
# 5.count the number of spaces in string
# msg="Welcome to ITP"
# space=[i for i in msg if i==" "]
# print(len(space))
# -------------------------------------------
# 6.find all the numbers from 1 to 100 that hav 3 in them
# sum=10
# list=[i for i in range(1,100) if "3" in str(i)]
# print(list)
# ---------------------------------------------
# 7. create lower and upper dictionary for ex. l=["ReD","GreEen","BLue"]
#   upper_lower_dict={'red':'RED','blue':'BLUE'....} using dc
# l=["ReD","GreEen","BLue"]
# upper_lower_dict={i.lower():i.upper() for i in l}
# print(upper_lower_dict)
# --------------------------------------------------
# 8. lets assume - I have on dict - original_dict={'jack':38,'James':33,'martin':46,'joe':27}
#     print only even values information in given dict.
#     means output will be - {'jack':38,'martin':46}
original_dict={'jack':38,'James':33,'martin':46,'joe':27}
new={key:val for key,val in original_dict.items() if val%2==0 }
print(new)