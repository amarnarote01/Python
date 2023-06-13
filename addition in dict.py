student={"name":"Amar","no":21,"m1":59,"m2":90,"m3":65}
sum=0
for key,val in student.items():
    if key=="m1" or key=="m2" or key=="m3":
        v=student[key]
        sum+=v
student.update({"total":sum})
print(student)
