#nasted loops star patterns
# ---------------------------------------------------------
# 1.
# *
# * *
# * * *
# * * * *
# * * * * *
# x=int(input("enter no"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# -----------------------------------------------------------
# 2.
# * * * * *
# * * * *
# * * *
# * * 
# *
# x=int(input("enter no"))
# for i in range(1,x+1):
#     for j in range(x+1,i,-1):
#         print("*",end=" ")
#     print()
# ------------------------------------------------------------
# 3.
# 1
# 12
# 123
# 1234
# 12345
# x=int(input("enter no"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# -------------------------------------------------------------
# 4.
# 12345
# 1234
# 123
# 12
# 1

# or
# x=int(input("enter no"))
# for i in range(x+1,1,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

# -------------------------------------------------------------------
# 5.
# 54321
# 5432
# 543
# 54
# 5
# x=int(input("enter no"))
# for i in range(0,x):
#     for j in range(x,i,-1):
#         print(j,end=" ")
#     print()
# ----------------------------------------------------------------------
# 6.
# 55555
# 4444
# 333
# 22
# 1
# x=int(input("enter no"))
# for i in range(x,0,-1):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()
# ---------------------------------------------------------------------
# 7.
# 11111
# 2222
# 333
# 44
# 5
# x=int(input("enter no"))
# for i in range(1,x+1):
#     for j in range(x+1,i,-1):
#         print(i,end=" ")
#     print()
# ---------------------------------------------------------------------
# 8.Multiplication table from 1 to 10
# x=int(input("enter no"))
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# ---------------------------------------------------------------------
# 9.
# A
# AB
# ABC
# ABCD
# x=int(input("enter no"))
# for i in range(1,x+1):
#     a=65
#     for j in range(1,i+1):
#         print(chr(a),end=" ")
#         a+=1
#     print()
#     or
# for i in range (65,71):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()
# -------------------------------------------
# 10.
# ABCD
# ABC
# AB 
# A
# x=int(input("enter no"))
# for i in range(1,x+1):
#     a=65
#     for j in range(x+1,i,-1):
#         print(chr(a),end=" ")
#         a+=1
#     print()
# ------------------------------------------------
# 11.
# 1
# 23
# 456
# 78910
# x=int(input("enter no"))
# a=1
# for i in range(1,x+1):
#     for j in range(x+1,i,-1):
#         print(a,end=" ")
#         a+=1
#     print()
# -------------------------------------------------
# 12.
#              1
#          1   2   1
#       1  2   3   2  1
#    1  2  3   4   3   2  1

# x=int(input("enter no of rows"))
# for i in range(1,x+1):
#     a=1
#     for j in range(x,i,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print(a,end=" ")
#         a+=1
#     for l in range(2,i+1):
#         print(a-2,end=" ")
#         a-=1
#     print()

#     # or 

# n=int(input("enter no"))
# for i in range(1,n+1):
#     for k in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#         if j==i:
#             for k in range(j-1,0,-1):
#                 print(k,end=" ")
#     print()

#  -----------------------------------------   #  
# normal pattern 
#           1
#          1  2
#         1  2  3  
# #       1  2  3  4  
# n=int(input("enter rows"))
# for i  in range(1,n+1):
#     for k in range(n,i,-1):
#         print(" ",end="")
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
# ----------------------------------------------------------
# 13.
#        A
#       B B
#     C  C  C
#   D  D  D  D
# E  E  E  E  E
# x=int(input("enter noof rows"))
# a=65
# for i in range(1,x+1):
#     for j in range(x,i,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print(chr(a),end=" ")
#     for l in range(2,i+1):
#         print(chr(a),end=" ")
#     a+=1
#     print()
# -----------------------------------------------------------
# 14.
#        *
#       * *
#     *  *  *
#   *  *  *  *
# *  *  *  *  *
# x=int(input("enter noof rows"))
# for i in range(1,x+1):
#     for j in range(x,i,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
#     for l in range(2,i+1):
#         print("*",end=" ")
#     print()
# -----------------------------------------------------------
# 15.
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# 
# x=int(input("enter noof rows"))
# for i  in range(0,x):
#     for j in range(0,x):
#         print("*",end=" ")
#     print()
# ----------------------------------------------------------
# 16.
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *
# x=int(input("enter no of rows"))
# x=(x//2)+1
# for i in  range(1,x+1):
#     for j in range(x,i,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
#     for l  in range(2,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for k in range(x,i,-1):
#         print("*",end=" ")
#     for l in range(i,x-1):
#         print("*",end=" ")
#     print()
# ------------------------------------------------
# 15.
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  ******* 
# x=int(input("enter no of rows"))
# x=(x//2)+1
# for i in range(1,x):
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for k in range(x,i,-1):
#         print("*",end=" ")
#     for l in range(i,x-1):
#         print("*",end=" ")
#     print()
# for i in  range(2,x):
#     for j in range(x,i,-1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
#     for l  in range(2,i+1):
#         print("*",end=" ")
#     print()
# -----------------------------------------
# 16.
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
# x=int(input("enter no of rows"))
# x=x+1
# for i in range(1,x):
#     a=1
#     for j in range(1,i+1):
#         print(" ",end=" ")
#     for k in range(x,i,-1):
#         print(a,end=" ")
#         a+=1
#     for l in range(i,x-1):
#         print(a,end=" ")
#         a+=1
#     print()
# or
# n=int(input("enter rows"))
# for i in range(n,0,-1):
#     for k in range(i,n+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()





