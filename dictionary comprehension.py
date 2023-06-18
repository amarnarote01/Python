# dictionary comprehrehension-it shortcut way to create dictionary
# 1. to create square dict from 1 to 10 numbers using Dictionary comprehrehension
# syntax
# dictionary_name={expression for loop}
# sq_dict={i:i*i for i in range(1,11)}
# print(sq_dict)
# ----------------------------------------
# 2.count of char
# msg="welcometoitprenure"
# count_dict={i:msg.count(i) for i in msg}
# print(count_dict)
# ----------------------------------------
# 3.for if else
# syntax
# for if
# list_name=[expression cond for loop if]
# for if else
# list_name=[expression if else cond for loop]
# 
# even odd number 
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_odd_dict={i:("even" if i%2==0 else "odd") for i in numbers}
# print(even_odd_dict)
# ---------------------------
# 4. create lower and upper dictionary for ex. l=["ReD","GreEen","BLue"]
#   upper_lower_dict={'red':'RED','blue':'BLUE'....} using dc
# l=["ReD","GreEen","BLue"]
# upper_lower_dict={i.lower():i.upper() for i in l}
# print(upper_lower_dict)
# --------------------------------------------------
# 5. lets assume - I have on dict - original_dict={'jack':38,'James':33,'martin':46,'joe':27}
#     print only even values information in given dict.
#     means output will be - {'jack':38,'martin':46}
# original_dict={'jack':38,'James':33,'martin':46,'joe':27}
# new={key:val for key,val in original_dict.items() if val%2==0 }
# print(new)
