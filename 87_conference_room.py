n,k = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(0,len(a)):
  if a[i] <= k:
    c += 1
print(c)
