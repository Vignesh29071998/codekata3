a,k=map(int,input().split())
b=list(map(int,input().split()))
flag=0
for i in range(0,a-1):
  for j in range(i+1,a):
    if b[i]+b[j]==k:
      flag=1
      break
    else:
      flag=0
  if flag==1:
     print('YES')
     break
else:
  print('NO')
