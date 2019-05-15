st = input()
c,i,j,a,ch,n = 1,0,1,'','',1
while i < len(st):
  c = 1
  while j < len(st):
    if st[i]==st[j]:
      c = c+1
      ch = st[i]
      j = j+1
    else:
      ch = st[i]
      j = j-1
      break
  else:
    ch = st[i]
  if c>1:
    n = c
  else:
    n = 1
  if n == 1:
    a = a+ch
  else:
    a = a+str(n)+'*'+ch
  i = j+1
  j = i+1
print(a) 
