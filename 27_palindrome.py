s=input()
st=''
for i in range(0,len(s)-1):
  st=s[:i+1]
  if st!=st[::-1]:
    a=st
print(a)
    
