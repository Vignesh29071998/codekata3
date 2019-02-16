n,k=map(int,input().split())
n1=list(map(int,input().split()))
c=0
for i in range(0,n-1):
  for j in range(i+1,n):
    if abs(n1[i]-n1[j])==k:
      c+=1
print(c)
