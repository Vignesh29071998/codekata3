n = int(input())
c = 0
for i in range(0,n+1):
  if i < 10 :
    c += 1
  else:
    j,p = 0,str(i)
    while j < len(p)-1:
      if abs(int(p[j])-int(p[j+1])) == 1:
        c += 1
      j += 1
print(c)
