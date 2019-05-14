a = list(input().split())
b,c = [],''
for i in range(0,len(a)):
  if i%2==0:
    for j in a[i]:
      if j != '.':
        c +=j
    b.append(c[::-1])
    c = ''
  else:
    b.append(a[i])
print(*b)
