a = input()
c,n,m = 0,'',0
for i in range(0,len(a)):
  c = 1
  for j in range(i+1,len(a)):
    if a[i]==a[j]:
      c += 1
    else:
      break
  if c>m:
    m = c
    n = a[i]
print(n,m)
    
