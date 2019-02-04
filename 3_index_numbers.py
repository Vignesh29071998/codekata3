a=int(input())
b=list(map(int,input().split()))
c=[]
flag=0
for i in range(0,a):
  if i==b[i]:
    c.append(i)
    flag=1
if flag==1:
  print(*c)
else:
  print('-1')
