import collections
n,k = map(int,input().split())
a,b,c = [],[],[]
for i in range(0,n):
  a.append(list(map(int,input().split())))
for i in range(0,n-1):
  for j in range(0,k):
    for l in range(0,k):
      if a[i][j]==a[i+1][l]:
        b.append(a[i][j])
        break
d = collections.Counter(b)
for i in b:
  if i not in c:
    if d[i]==n-1:
      c.append(i)
print(*sorted(c))
