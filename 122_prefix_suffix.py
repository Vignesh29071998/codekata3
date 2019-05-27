n = int(input())
a = list(map(int,input().split()))
for i in range(1,n-1):
  if sum(a[:i]) == sum(a[i+1:]):
    print('yes')
    break
else:
  print('no')
