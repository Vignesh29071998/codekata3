s = input().split()
p,l,m = '',[],0
for i in range(0,len(s)):
  for j in range(0,len(s[i])):
    m += 1
    if m%2 != 0:
      p += s[i][j].upper()
    else:
      p += s[i][j]
  l.append(p)
  p = ''
print(*l)

