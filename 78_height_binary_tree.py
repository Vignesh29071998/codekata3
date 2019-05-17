n,m = map(int,input().split())
a,b,l = [],[],0
for i in range(0,m):
  a.append(list(map(int,input().split())))
while l < len(a):
  for j in range(l+1,len(a)):
    if a[l][0]==a[j][0]:
      b.append([a[l],a[j]])
      break
  l = l+1
print(len(a)-len(b)+1)
  
