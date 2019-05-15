a = input()
b,m,i = list(a),0,0
while i < len(a)-1:
  if a[i]==a[i+1]:
    del b[i]
    i = i+2
    if int(''.join(b))>m:
      m = int(''.join(b))
      b = list(a)
  else:
    i = i+1
print(m)
