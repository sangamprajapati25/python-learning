from array import*
student = array ('i',[101,102,103,104,105])
s = 0
while (s<(len(student))):
    print(s,student[s])
    s+=1
print('after this we will see append')
student.append(106)
student.append(107)
s =0
while (s<(len(student))):
    print(s, student[s])
    s+=1
    