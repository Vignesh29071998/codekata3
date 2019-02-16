a=input()
s=''
for i in range(0,len(a)-2,2):
  if a[i]=='a' and a[i+1]=='b' and i!=len(a)-1:
    s+=a[i]+a[i+1]
  else:
    s=''
b=len(a)-1
if a[b]=='a' and a[b-1]=='b' and s!='':
  s+=a[b]
print(len(s))
    
    
