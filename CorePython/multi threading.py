# Multitasking:
# capability of Performing multiple task simultaneously/ability of OS to perform different tasks at the same time.
# •Two-types of multitasking:
# 1)process
# 2 Thread
# Thread: It is basically an independent flow of execution.

# ============================================================================================================================================
#Implement multithreading using extending thread class:
# from threading import Thread
#
# class MyTrd1(Thread):
#     def run(self) -> None:
#         for i in range(1,100):
#             print("Hi from MyTrd1 class......")
#
# class MyTrd2(Thread):
#     def run(self) -> None:
#         for i in range(1,20):
#             print("Hi from MyTrd2 class......")
#
# t1=MyTrd1()
# t2=MyTrd2()
# t1.start()
# t2.start()

# ============================================================================================================================================
# Without extending thread class
# from threading import *
# class demo:
#     def B(self):
#         lst=[2,3,44,'w','abc']
#         for x in lst:
#             print("child prinitng",x)

# myobj=demo()
# t1=Thread(target=myobj.B)
# print("After the class statement")
# t1.start()
# print("done.....")  
# ---------------------------------------------------------------------------------------------------------

#  without using class 
# from threading import *
# def new():
#     for x in range(60):
#         print("Welcome")
# t1=Thread(target=new)
# print("I am in main")
# t1.start()
 # t1.join()  # one thread waits for another thread to complete its task first then the processor will execute the next function
# print("bye")
# =========================================================================================================================
# from threading import *
# from time import sleep
# class Medical(Thread):
#     def run(self):
#         print("Medical Start....")
#         sleep(2)
#         print("Medical Test Completed")
# class Testdrive(Thread):
#     def run(self):
#         print("Testdrive Start....")
#         sleep(2)
#         print("Testdrive Test Completed")
# class Officer(Thread):
#     def run(self):
#         print("Officer are working in progress ....")
#         sleep(2)
#         print("Officer work Completed...Now collect Licence")     
# t1=Medical()
# t1.start()
# t1.join()
# t2=Testdrive()
# t2.start()
# t2.join()
# t3=Officer()
# t3.start()
# ==============================================================================================================================
  