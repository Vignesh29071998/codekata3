a,b = input().split()
c,s = 0,''
for i in range(0,len(a)):
  k = i
  for j in range(0,len(b)):
    if a[k] == b[j]:
      s += a[k]
      k += 1
    else:
      break
  if len(s) > c:
    c = len(s)
    p = s
  s = ''
print(p)
    

