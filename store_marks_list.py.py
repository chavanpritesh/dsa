marks=[]
rollno=[]
trollno=[]
t=int(input("Enter the strenth of class"))
for i in range(t):
    m=int(input("Enter roll no of student:"))
    trollno.append(m)
print("roll no of total student:",trollno)    

N=int(input("Enter total no of student present for exam:"))
for i in range(N):
    m=int(input("roll no of student"))
    rollno.append(m)
print("Roll No of present student:",rollno)
for i in range(N):
    m=int(input("mark of student"))
    marks.append(m)
print("marks of present student:",marks)

#average
sum=0
for i in range(N):
        sum=sum+marks[i]
avr=sum//N
print("The average score is:",avr)

#high
high=marks[0]
for i in range(N):
    if high<marks[i]:
        high=marks[i]
print("The highest score is:",high)

#low
low=marks[0]
for i in range(N):
    if low>marks[i]:
        low=marks[0]
print("lowest mark obtained:",low)

#count of absent student
print("count of absent student:",t-N) 
print("roll no of absent student:",set(trollno).difference(rollno))

#frequncy
print("maximum frequncy:",max(marks,key=marks.count))           