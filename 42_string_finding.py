s = "WELCOMETOGUVICORPORATIONS"
u = input()
a,b,c,k,flag = [],[],[],0,0
def find(m,n,m1,n1,a1,b1):
  p,l = m+m1,n+n1
  for i in range(2,len(u)):
    try:
      if c[p][l] == u[i]:
        flag = 1
        s1,s2,e1,e2 = a1,b1,p,l
      else:
        flag = 0
        e1,e2 = 0,0
        break
    except IndexError:
      flag = 0
      break
    p,l = p+m1,l+n1
  if flag == 1:
    print(s1-1,s2-1)
    print(e1-1,e2-1)
  return flag
for i in range(0,len(s),5):
  for j in range(0,5):
    a.append(s[i+j])
  b.append(a)
  a = []
for i in range(0,len(b)+2):
  if i == 0 or i == len(b)+1:
    c.append([0]*7)
  else:
    p = [0] + b[i-1] + [0]
    c.append(p)
for i in range(1,len(c)-1):
  for j in range(1,len(c)-1):
    if c[i][j] == u[k]:
      x,y = i,j
      if c[x-1][y] == u[k+1]:
        s=find(x-1,y,-1,0,x,y)
      if c[x][y-1] == u[k+1]:
        s=find(x,y-1,0,-1,x,y)
      if c[x+1][y] == u[k+1]:
        s=find(x+1,y,1,0,x,y)
      if c[x][y+1] == u[k+1]:
        s=find(x,y+1,0,1,x,y)
      if c[x-1][y-1] == u[k+1]:
        s=find(x-1,y-1,-1,-1,x,y)
      if c[x+1][y-1] == u[k+1]:
        s=find(x+1,y-1,1,-1,x,y)
      if c[x+1][y+1] == u[k+1]:
        s=find(x+1,y+1,1,1,x,y)
      if c[x-1][y+1] == u[k+1]:
        s=find(x-1,y+1,-1,1,x,y)
    if s == 1:
      break
  if s == 1:
    break
else:
  print('0')
