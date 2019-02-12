a=input()
b=[]
for i in a:
  b.insert(0,i)
c=''.join(b)
if a==c:
  print('YES')
else:
  print('NO')
  
