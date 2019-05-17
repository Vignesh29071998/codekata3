s = input().split()
st,a = '',[]
for i in range(0,len(s)):
  for j in range(0,len(s[i])):
    if j%2 == 0:
      st += s[i][j].upper()
    else:
      st += s[i][j]
  a.append(st)
  st = ''
print(*a)
