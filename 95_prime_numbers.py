n = int(input())
a,flag = [],0
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
if a==[]:
  print('0')
else:
  print(*a)
