n = int(input())
a,su = [],0
for i in range(0,n):
  a.append(list(map(int,input().split())))
for i in range(0,n):
  for j in range(0,n):
    su = su+a[i][j]
b = su / n**2
print('%.6f' %b)
