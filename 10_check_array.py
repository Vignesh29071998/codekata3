a,b=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
flag=0
if a>b:
  for i in b1:
    if i in a1:
      flag=1
    else:
      flag=0
  if flag==1:
    print('YES')
  else:
    print('NO')
else:
  print('NO')
      
