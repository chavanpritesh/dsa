name,game_c,game_b,game_f,set_1,set_2,set_3,set_4 = [],[],[],[],[],[],[],[]
j,c,b,f=0,0,0,0

def list_input(a):
  global j
  count=0
  char=""
  for i in range(0,len(a)):
    if (a[i]!=","):
      char+=a[i]  
    else:
      if (j==0):
        name.append(char)
      elif (j==1):
        game_c.append(char)
      elif (j==2):
        game_b.append(char)
      elif (j==3):
        game_f.append(char)      
      count+=1
      char=""
  j+=1

list_input(input("Enter the universal set of students in A,B,C format :\n")+",")
list_input(input("Enter the set of students playing CRICKET :\n")+",")
list_input(input("Enter the set of students playing BADMINTON :\n")+",")
list_input(input("Enter the set of students playing FOOTBALL :\n")+",")

for i in name:
  if i in game_c:
    c=1
  if i in game_b:
    b=1
  if i in game_f:
    f=1     
  if (c==1 and b==1):
    set_1.append(i)
  if ((c==0 and b==1) or (c==1 and b==0)):
    set_2.append(i)
  if (c==0 and b==0):
    set_3.append(i)
  if (c==1 and b==0 and f==1):
    set_4.append(i)            
  c,b,f=0,0,0    

print("Total number of students is : "+str(len(name))+"\n"+str(set(name)))    
print("Students who play both badminton and cricket are : "+str(len(set_1))+"\n"+str(set(set_1)))  
print("Students who play either badminton or cricket but not both are : "+str(len(set_2))+"\n"+str(set(set_2)))  
print("Students who play neither badminton nor cricket are : "+str(len(set_3))+"\n"+str(set(set_3))) 
print("Students who play both football and cricket but not badminton are : "+str(len(set_4))+"\n"+str(set(set_4)))
