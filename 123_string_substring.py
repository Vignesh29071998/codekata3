a,b = input().split()
for i in range(0,len(a)-len(b)+1):
  if a[i:len(b)+i] == b:
    print('yes')
    break
else:
  print('no')
