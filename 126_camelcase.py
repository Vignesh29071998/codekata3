s = input().split()
flag = 0
for i in s:
  if i[0].isupper():
    flag = 1
  else:
    flag = 0
    break
if flag == 1:
  print('yes')
else:
  print('no')
