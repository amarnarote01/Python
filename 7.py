"""4. To ask user that how many days in a leap year. 

a. if user will get correct ans -
      then print "You have cleared the first level" and ask again another que "What month has an extra day in leap year?" if user will get correct answer then display message "Congratulations !!You have cleared the test" otherwise "You have failed the test".

b.otherwise print following msg-

      "Your input is wrong, please try again."""
 

x=int(input("how many days in a leap year? "))
if x==366:
    print("You have cleared the first level")
    y=input("What month has an extra day in leap year? ")
    if y=="feb" :
        print("Congratulations !!You have cleared the test")
    else:
        print("You have failed the test")
else :
    print("Your input is wrong, please try again.")

