n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
b = []
if n%2 == 0:
  for i in range(0,n//2):
    b.append(a[(n-1)-i])
    b.append(a[i])
else:
  for i in range(0,(n//2)+1):
    if i != (n//2):
      b.append(a[(n-1)-i])
      b.append(a[i])
    else:
      b.append(a[i])
print(*b)

