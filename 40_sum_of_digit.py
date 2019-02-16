a=input()
s=0
for i in a:
  s+=int(i)
b=str(s)
if b==b[::-1]:
    print('YES')
else:
  print('NO')
