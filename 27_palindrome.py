s=input()
st=''
for i in range(0,len(s)-1):
  st=s[:i+1]
  if st!=st[::-1]:
    a=st
    flag=1
  else:
    flag=0
if flag==1:
  print(a)
else:
  print(s)
  
  

    
  

    
