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
for i in range(0,len(a)-1):
  for j in range(i+1,len(a)):
    if a[i]+a[j] == n:
      print(a[i],a[j])
      indic = 1
      break
  if indic == 1:
    break
