n = int(input())
a,c = [],0
for i in range(1,n+1):
  b = str(i)
  for j in range(0,len(b)):
    if b[j]=='2':
      c += 1
print(c)
    
