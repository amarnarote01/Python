# The vending machine displays a welcome message with all products and prices
# The vending machine asks the user to select a product
# The Vending machine asks the user to enter coins. The coins accepted are 5,10,20,50,100 cents
# The Vending machine calculates the total money inserted
# Calculate the change amount
# Calculate the minimum number of coins to return
# Display the change amount and coins to the user
def purchase_product():
    print("Welcome")
    Display()
    x=int(input("Enter Sr.no. of Item want to buy:"))
    if x in Products:
        for key,val in Products.items():
            if key==x:
                for k,v in val.items():
                    if k=='price':
                        print(f"price ={v}")
    else:
        print("Invalid choice")
        a=input("Want to Try again type Y for Yes N for No-")
        if a=="y" or a=="Y":
            purchase_product()
        else:
            print("Thank You!!")
    payment(v)
    a=input("\nWant to purchase another product type Y for Yes N for No-")
    if a=="y" or a=="Y":
        purchase_product()
    else:
        print("Thank You!!")
        
def payment(v):
    while True:
        print("\nOnly Accepted coins are 5 10 20 50 100\n")
        pay=int(input(f"complete payment of {v} to buy and  enter coin: "))
        if pay==5 or pay==10 or pay==20 or pay==50 or pay==100:
            if pay==v:
                print("Collect Your Product\nThank You!!")
                break
            elif v-pay<0:
                print(f"your change {pay-v}\nCollect Your Product\nThank You!!")
                break
            else:
                v=v-pay
        else:
            print("Invalid Amount!!")
            a=input("Want to try payment again type Y for Yes N for No-")
            if a=="y" or a=="Y":
               payment(v)
               break
            else:
               print("Thank You!!")
               break

def Display():
    print("Products list")
    for key,val in Products.items():
        print(f"Sr.no{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")

Products={ 1:{'product_name':'Coke','price':20},
          2:{'product_name':'Chips','price':35},
          3:{'product_name':'7up','price':30},
          4:{'product_name':'Maaza','price':50},
          5:{'product_name':'Limka','price':25},
          6:{'product_name':'Biscuit','price':10},
          7:{'product_name':'Pepsi','price':25},
          8:{'product_name':'Cake','price':100},
          9:{'product_name':'Chocolate','price':40},
          10:{'product_name':'Soda','price':20}
          }
purchase_product()
