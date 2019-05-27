n =int (input())
a = []
for i in range(0,n):
  for j in range(0,n-i):
    a.append(1)
  print(*a)
  a = []
    
