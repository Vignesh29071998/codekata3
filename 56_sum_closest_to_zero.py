n = int(input())
a = list(map(int,input().split()))
m = 1000
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    if abs(a[i]+a[j]) < m:
      m = abs(a[i]+a[j])
      p,l = a[i],a[j]
print(p,l)
