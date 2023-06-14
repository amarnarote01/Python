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
L=['a',['bb','cc'],'d']
L[1].append('xx')
print(L)
L[1].insert(1,'zz')
print(L)
L[1].extend([1,2,3])
print(L)
