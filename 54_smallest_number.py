n=int(input())
a=list(map(int,input().split()))
i=0
while i<n-1:
  if a[i]<a[i+1]:
    a[i],a[i+1]=a[i],a[i]
    i+=1
  else:
    i+=1
print(*a)
