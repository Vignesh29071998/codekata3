n = int(input())
a,su = [],0
for i in range(0,n):
  a.append(list(map(int,input().split())))
  su += a[i][i]
print(su)
