a=input()
s=''
m=0
i=0
while i<len(a)-1:
  if a[i]=='a' and a[i+1]=='b':
    s+=a[i]+a[i+1]
    i+=2
  else:
    s=''
    i+=1
  if m<len(s):
    m=len(s)
b=len(a)-1
if a[b]=='a' and a[b-1]=='b' and s!='':
  m+=1
print(m)
    
    

    
