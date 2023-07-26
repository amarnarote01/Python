
# None selected 

# Skip to content
# Using Gmail with screen readers
# in:sent 
# Conversations
# 9.42 GB of 15 GB used
# Terms · Privacy · Program Policies
# Last account activity: 0 minutes ago
# Open in 1 other location · Details
# Name :Amar Narote

# 1. Find all of the words in a string that are less than 4 letters using List comprehension.
 
# list= ["john","don","shawn","Sam","miky","Martin"]
# list2=[i for i in list if len(i)<4 ]
# print(list2)


# 2.Count the number of spaces in a string using list comprehension.

# str="Python is high level programming language"
# list2=[i for i in str if i==" " ]
# print(len(list2))


# 3.Find all of the numbers from 1-1000 that have a 3 in them using list comprehension.

# list2=[i for i in range(1,1001) if '3' in str(i) ]
# print(list2)

# 4.make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# list=[]
# for i in fruits:
#     count=0
#     if 'a' in i:
#         count+=1
#     if 'e' in i:
#         count+=1
#     if 'i' in i:
#         count+=1
#     if 'o' in i:
#         count+=1
#     if 'u' in i:
#         count+=1
#     if count==2:
#         list.append(i)
# print(list)
# 5.make a list that contains each fruit with exactly 5 characters.

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# list=[i for i in fruits if len(i)==5]
# print(list) 


# 6.Make a list that contains fruits that have less than 5 characters

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# list=[i for i in fruits if len(i)<5]
# print(list)


# 7.Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# list=[len(i) for i in fruits]
# print(list)

# 8.create 10 students dictionary and print highest marks student dictionary

dict={"student1":80,"student2":70,"student3":90,"student4":85,"student5":65,"student6":95,"student7":67,"student8":56,"student9":87,"student10":55}
list=[]
for value in dict.values():
    list.append(value)
        
for key,value in dict.items():
    if value==max(list):
        print(key,value)
# 9. Create nested list containing values as the count of list items.

# for Ex. - Input: [1, 2, 3]
# Output: [[1], [2, 2], [3, 3, 3]]

# Input: [4, 5]
# Output: [[1, 1, 1, 1], [2, 2, 2, 2, 2]]
# # ans:-

# list=[1,2,3]
# list2=[]
# print(list)
# for i in list:
#     list1=[]
#     for j in range(i):
#         list1.append(i)
#     list2.append(list1)
# print(list2)

# 10.Remove Negative Elements in List.
# list=[1,2,-3,6,-9,10,-23,56]
# list2=[i for i in list if i>0]
# print(list2)
