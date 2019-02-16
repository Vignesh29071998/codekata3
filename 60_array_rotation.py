n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
i=5
while i>0:
  d=a.pop(0)
  a.append(d)
  if a!=b:
    c+=1
    i-=1
  else:
    c+=1
    break
print(c)
    
