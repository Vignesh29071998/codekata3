a,b=map(int,input().split())
c=list(map(int,input().split()))
i=0
while i<b:
  d=c.pop(0)
  c.append(d)
  i+=1
print(*c)
