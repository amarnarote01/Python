guess_no=444

x=1
while(x!=6):
    n=int(input("Enter Gussing no"))
    if n==guess_no:
        print(f"Your correct in {x} chance")
        break
    elif n in range(400,444):
        print("Your close ")
    elif n in range(445,500):
        print("Your close ")
    elif n in range(300,400):
        print("Your low")
    elif n in range(500,600):
        print("Your  High")
    elif n in range(200,300):
        print("Your too low")
    elif n in range(600,700):
        print("Your too high")
    elif n<200:
        print("very very low")
    elif n>700:
        print("very very high")
    x+=1
# if x==6:  
# or 
else:
    print("You have failed all 5 chances!! ")