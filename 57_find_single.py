a=int(input())
b=list(map(int,input().split()))
d={}
for i in b:
  if i not in d:
    d[i]=1
  else:
    d[i]+=1
print(min(d,key=d.get))
