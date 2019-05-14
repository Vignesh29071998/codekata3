s = input()
t = input()
a,b,s1,t1,m = [],[],'','',0
for i in range(0,len(s)-1):
  for j in range(i,len(s)):
    s1 = s1+s[j]
    a.append(s1)
  s1 = ''
for i in range(0,len(t)-1):
  for j in range(i,len(t)):
    t1 = t1+t[j]
    b.append(t1)
  t1 = ''
for i in a:
  if i in b and len(i)>=m:
    m = len(i)
    k = i
print(k)
