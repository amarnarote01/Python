#palindrome
l=["john","martin","scott","smith","mom","madam"]
pallin_dict={}
for i in l:
    if i[::-1]==i:
        pallin_dict.update({i:"pallindrome"})
    else:
        pallin_dict.update({i:"not pallindrome"})
print(pallin_dict)


#create character count dictonary from given string
#{'w': 1, 'e': 4, 'l': 1, 'c': 1, 'o': 2, 'm': 1, 't': 2, 'i': 1, 'p': 1, 'r': 2, 'n': 1, 'u': 1}
message="welcometoitprenure"
char_count_dict={}
for i in message:
    char_count_dict.update({i:message.count(i)})
print(char_count_dict)

#reverse dictonary print {'john': 'nhoj', 'martin': 'nitram', 'scott': 'ttocs', 'smith': 'htims', 'mom': 'mom', 'madam': 'madam'}
l=["john","martin","scott","smith","mom","madam"]
rev_dict={}
for i in l:
        rev_dict.update({i:i[::-1]})
print(rev_dict)

#remove all occurences of specific item in list 
#using for
list1=[23,45,67,23,56,78,23,89,90,23,23]
no=23
for i in list1:
     if i==no:
        list1.remove(i)
list1.remove(no)
print(list1)

#sort list in ascending or descinding
list1.sort(reverse=True) #decending 
print(list1)
list1.sort() #ascending
print(list1)

#without using inbuild function remove all occurences of specific item in list
list1=[23,45,67,23,56,78,23,89,90,23]
no=23
list2=[]
for i in range(0,len(list1)):
     if list[i]==23:
        continue
     else:
        list2=list2+[list1[i]]
print(list2)
#scearching  with "in"
search=int(input("enter no want to search"))
if search in list1:
    print("number is present")
else:
    print("number is not present")


#remove user defined key and value pair u want to delete form dictonary
student={"name":"Rohit","age":45,"course":"python"}
x=input("enter key u want to delete")
student.pop(x) 
print(student)

