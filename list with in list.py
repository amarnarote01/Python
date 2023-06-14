# l=['a','b',['cc','dd',['eee','fff']],'g','h']
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[2][1])
# print(l[2][2])
# print(l[2][2][0])
# print(l[2][2][1])
# print(l[3])
# print(l[-3])
# -------------------------------
# L=['a',['bb','cc','dd'],'e']
# L[1].append('xx')
# print(L)
# L[1].insert(1,'zz')
# print(L)
# L[1].extend([1,2,3])
# print(L)
# x=L[1].pop(1)
# print(L)
# print(len(L[1]))
# -------------------------------------
# loop with in loop
# l=[[1,2,3],[3,4,5],[5,6,7]]
# print(l[0])
# print(l[1])
# print(l[2])
# for i in l:
#     for j in i:
#         print(j)
# # add 
# for i in l:
#     sum=0
#     for j in i:
#         sum+=j
#     print(f"sum of l[{i}]={sum}")
