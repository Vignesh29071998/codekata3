l=input().split()
s=''
for i in range(0,len(l)):
  if i==len(l)-1:
    s=l[i]
    print(s[::-1])
  else:
    s=l[i]
    print(s[::-1],end=' ')
    s=''
  
