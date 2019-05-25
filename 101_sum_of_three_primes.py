n = int(input())
a,flag,indic = [],0,0
for i in range(2,n):
  for j in range(2,i):
    if i%j == 0:
      flag = 0
      break
    else:
      flag = 1
  if i == 2:
    a.append(i)
  if flag == 1:
    a.append(i)
for i in range(0,len(a)-2):
  for j in range(i,len(a)-1):
    for k in range(j,len(a)):
      if a[i]+a[j]+a[k] == n:
        print(a[i],a[j],a[k])
        indic = 1
        break
    if indic == 1:
      break
  if indic == 1:
    break
