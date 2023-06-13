#add user defined list and print the addition of nos which is divisible by 3 and 5
"""l= [int(x) for x in input("enter nos").split()]
sum=0
for i in l:
    if i%3==0 and i%5==0:
        sum=sum+i
print(sum)"""
#add new number in specific position
"""no=int(input("enter no"))
position=int(input("enter position"))
l.insert(position,no)
print(l)"""
#add user defined names in list and print names on output screen which length >=4
"""names=input("enter names").split()
for i in names:
    if len(i)>=4:
        print(i) 
print(names)"""
#add user defineed names in list and which length >=4 add 
#this element in A list and remaining names add in B list
"""names=input("enter names\n").split()
a=[]
b=[]
for i in names:
    if len(i)>=4:
        a.append(i) 
    else:
        b.append(i)
print(a)
print(b)"""
#to check how many time word repeated 
"""para ='''Python is high level programming language . Python is very easy to learn
         for data science and machine lerning application '''
char_count={}
l=para.split()
for i in l:
    count = l.count(i)
    char_count.update({i:count})
print(char_count)"""
#create list and add numbers in list .
# then create 2 different list that is square and cube list if number 
# is even then add in squar list and number is odd then add in cube list .
# and perform square of even nos and cube of add nos
"""l= [int(x) for x in input("enter nos ").split()]
square=[]
cube=[]
for i in l:
    if i%2==0:
        i=i*i
        square.append(i) 
    else:
        i=i*i*i
        cube.append(i)
print("square =",square)
print("cube=",cube)"""
