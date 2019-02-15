a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,a):
  if i==0:
    p=1
    d=b[i+1:]
    for i in d:
      p=p*i
    c.append(p)
  elif i==a-1:
    p=1
    d=b[:i]
    for i in d:
      p=p*i
    c.append(p)
  else:
    s1,s2=b[:i],b[i+1:]
    p1,p2=1,1
    for i in s1:
      p1=p1*i
    for i in s2:
      p2=p2*i
    c.append(p1*p2)
print(*c)
