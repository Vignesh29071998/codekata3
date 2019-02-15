a,b=map(int,input().split())
c,count,flag=0,0,0
for i in range(a,b+1):
  c=0
  bi=bin(i)
  for i in range(0,len(bi)):
    if bi[i]=='1':
      c+=1
  if c==2:
      count+=1
  elif c>2:
    for i in range(2,c):
      if c%i==0:
        flag=1
        break
      else:
        flag=0
    if flag==0:
      count+=1
print(count)
   
