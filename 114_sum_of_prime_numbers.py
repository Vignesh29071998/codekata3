l,r = map(int,input().split())
def prime(l,r):
  c,flag = [],0
  for i in range(l,r+1):
    for j in range(2,i):
      if i%j == 0:
        flag = 0
        break
      else:
        flag = 1
    if i == 2:
      c.append(i)
    if flag == 1:
      c.append(i)
  return c
m = 0
for i in range(l,r+1):
  k,s = str(i),0
  if len(k) > 1:
    for j in range(0,len(k)):
      s += int(k[j])
    l = prime(2,s)
    if s in l:
      m += 1
  else:
    u = prime(2,i)
    if i in u:
      m += 1
print(m)
