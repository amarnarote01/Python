
def menu():
    print("Menu")
    print("1. Add new Product")
    print("2. show all product")
    print("3. Update specific product")
    print("4. Delete product")
    print("5. purchase product")
    x=int(input("Select from above and Enter no -"))
    if x==1:
        add_product()
    elif x==2:
        show_all_product()
    elif x==3:
        update_product()
    elif x==4:
        delete_product()
    elif x==5:
        purchase_product()
    else:
        print("invalid choice")
        x =input("Want to try again type Y for Yes N for No-")
        if x=="y" or x=="Y":
          menu()
        else:
            print("Thank You!!")

def add_product():
    print(f"There are {len(grossary)} products on stock")
    x=int(input("Enter how many products Want to Add"))
    for i in range(0,x):
        key=input("enter Sr.no.:-")    
        val={}
        for i in range(4):
            if i==0:
                k='product_id'
                v=int(input("Enter product_id:-"))
            if i==1:
                k='product_name'
                v=input("Enter product_name:-")
            if i==2:
                k='stock'
                v=int(input("Enter stock:-"))
            if i==3:
                k='price'
                v=int(input("Enter price:-"))
            val.update({k:v})
            grossary.update({key:val})
            print("--------------------")
    for key,val in grossary.items():
        print(f"Sr.no{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")
    
    a=input("Want to enter menu again type Y for Yes N for No-")
    if a=="y" or a=="Y":
        menu()
    else:
        print("Thank You!!")


def show_all_product():
    for key,val in grossary.items():
        print(f"Sr.no{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")
    a=input("Want to enter menu again type Y for Yes N for No-")
    if a=="y" or a=="Y":
        menu()
    else:
        print("Thank You!!")



def update_product():
    x=grossary.copy()
    print("Want to update product")
    s=(int(input("Enter sr.no.")))
    for key,val in x.items():
        if key==s:
            for k,v in val.items():
                if k=='product_id':
                    val[k]=int(input("Enter product_id want to change to:-"))
                if k=='product_name':
                    val[k]=input("Enter product_name want to change to:-")
                if k=='stock':
                    val[k]=int(input("Enter stock want to change to :-"))
                if k=='price':
                    val[k]=int(input("Enter price want to change to :-"))
    for key,val in grossary.items():
        print(f"Sr.no{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")
    a=input("Want to enter menu again type Y for Yes N for No-")
    if a=="y" or a=="Y":
        menu()
    else:
        print("Thank You!!")

def delete_product():
    s=(int(input("Enter sr.no.of product want o delete")))
    grossary.pop(s)

    for key,val in grossary.items():
        print(f"Sr.no{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")

    a=input("Want to enter menu again type Y for Yes N for No-")
    if a=="y" or a=="Y":
        menu()
    else:
        print("Thank You!!")

def purchase_product():
    print("List of products")
    for key,val in grossary.items():
        print(f"Sr.no:{key}:-")
        for k,v in val.items():
            print(f"{k}-{v}")
        print("---------------------")
    x=int(input("Enter Sr.no. of Item want to buy"))
    y=int(input("Enter quantity of product"))
    z=grossary.copy()
    for key,val in z.items():
        if key==x:
            for k,v in val.items():
                if k=='price':
                    print(f"price ={v*y}")
    payment(v,y)

    a=input("Want to enter menu again type Y for Yes N for No-")
    if a=="y" or a=="Y":
        menu()
    else:
        print("Thank You!!")

def payment(v,y):
    pay=int(input(f"complete payment of {v*y} to buy "))
    if pay==v*y:
        print("Your order has been placed\nThank You!!")
    else:
        print("Invalid Amount!!")
        a=input("Want to try payment again type Y for Yes N for No-")
        if a=="y" or a=="Y":
            payment(v,y)
        else:
            print("Thank You!!")

grossary={ 1:{'product_id':101,'product_name':'Maggie','stock':100 ,'price':25},
          2:{'product_id':102,'product_name':'Biscuits','stock':200 ,'price':10},
          3:{'product_id':103,'product_name':'Atta','stock':150 ,'price':100},
          4:{'product_id':104,'product_name':'Pasta','stock':100 ,'price':30},
          5:{'product_id':105,'product_name':'Chips','stock':300 ,'price':20},
          6:{'product_id':106,'product_name':'Chocolate','stock':500 ,'price':50},
          7:{'product_id':107,'product_name':'Toothbursh','stock':100 ,'price':35},
          8:{'product_id':108,'product_name':'Soap','stock':250 ,'price':45},
          9:{'product_id':109,'product_name':'Powdwer','stock':150 ,'price':70},
          10:{'product_id':110,'product_name':'Roomfreshner','stock':200 ,'price':80}
          }
menu()
