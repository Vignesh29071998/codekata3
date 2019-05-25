n,m = map(int,input().split())
a,c,flag = [],1,0
for i in range(0,m):
  a.append(list(map(int,input().split())))
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    if a[i][0] == a[j][0]:
      c += 1
    if c > 2:
      flag = 0
      break
    else:
      flag = 1
  c = 0
  if flag == 0:
    print('NO')
    break
if flag == 1:
  print('YES')
