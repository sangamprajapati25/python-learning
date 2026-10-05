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

#getting user input to append in array using for loop 

from array import*
student = array ('i',[])
n = int(input('enter the number of elements: '))
for i in range(n):
    student.append(int(input('enter the elements: ')))
for i in range(len(student)):
        print(i,student[i])
 

#getting user input to append in array using while loop 
from array import*
student = array('i',[])
n = int(input('Enter the number of elements'))
i = 0
while i<n:
    student.append(int(input('Enter the elelments')))
    i+=1
j =0
while j<(len(student)):
    
    print(j,student[j])
    j+=1
   




    
