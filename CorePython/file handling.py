# file handling 
# 1.text mode 
# 2.binary mode
# ------------------------------------------------------
# pickle:
# import pickle
# car=["Audi","BMW","Maruti Suzuki","Harryti Tuzuki"]
# fileobj=open("mycar.pkl",'wb')
# pickle.dump(car,fileobj)
# fileobj.close()

# # unpickle

# fileobj=open("mycar.pkl",'rb')
# x=pickle.load(fileobj)
# print(x)

# -------------------------------------------------------
# user_info=input("entr information")
# try:
#     with open("Fp.text",'a+') as fp:
#         fp.write(user_info)
#         print("data added sucessfully")
#         fp.seek(0)
#         print(fp.read())
# except Exception as e:
#     print("there is some problem",e)
# print("jsjabihjinaiz")

# --------------------------------------------------
# try:
#     fp=open("Fp.text",'r')
#     print(fp.read())
#     fp.close()
# except IOError:
#     print("File not found please check")
# finally:
#     print("exit")
# ---------------------------------------------------
import pickle
car=["Audi","BMW","Maruti Suzuki","Harryti Tuzuki"]
fileobj=open("mycar.pkl",'wb')
pickle.dump(car,fileobj)
fileobj.close()
fileobj=open("mycar.pkl",'rb')
x=pickle.load(fileobj)
print(x)