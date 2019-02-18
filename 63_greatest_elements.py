a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,a):
  if i==a-1:
    break
  else:
    c.append(max(b[i+1:]))
c.append(0)
print(*c)
