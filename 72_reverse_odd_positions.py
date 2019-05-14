a = list(input().split())
b = []
for i in range(0,len(a)):
  if i%2==0:
    c = a[i]
    b.append(c[::-1])
  else:
    b.append(a[i])
print(*b)

