n,m = map(int,input().split())
def prime(a):
  flag = 0
  if a == 2:
    flag = 1
  else:
    for i in range(2,a+1):
      for j in range(2,i):
        if i%j == 0:
          flag = 0
          break
        else:
          flag = 1
  return flag
a,b =prime(n),prime(m)
if a==b==1:
  print('yes')
else:
  print('no')
