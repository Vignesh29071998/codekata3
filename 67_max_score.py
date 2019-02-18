a=input().split('#')
b=input().split('#')
a1,b1=0,0
for i in a:
  if i.isdigit():
    a1+=int(i)
for i in b:
  if i.isdigit():
    b1+=int(i)
if a1>b1:
  print(a[0])
else:
  print(b[0])
    
