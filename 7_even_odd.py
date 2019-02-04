a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,a):
  if i%2==0 and b[i]%2!=0:
    c.append(b[i])
  elif i%2!=0 and b[i]%2==0:
    c.append(b[i])
print(*c)
       
  
