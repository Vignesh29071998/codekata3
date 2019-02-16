a=int(input())
b=list(map(int,input().split()))
u,v=map(int,input().split())
c=[]
flag=0
for i in range(0,a):
  if b[i]==u or b[i]==v:
    c.append(b[i])
    for j in range(i+1,a):
      if b[j]==u or b[j]==v:
        c.append(b[j])
        flag=1
        break
      else:
        c.append(b[j])
  if flag==1:
    break
print(len(c)-1)
