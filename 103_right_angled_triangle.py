n = int(input())
k,a = 0,[]
for i in range(0,n):
  for j in range(0,1+k):
    a.append(1)
  print(*a)
  a = []
  k += 2
