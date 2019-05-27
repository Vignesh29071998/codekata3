s = input().lower()
c,a,l = 0,[],''
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    p = s[i:j+1]
    if len(p)>1:
      if p == p[::-1]:
        if len(p) > c:
          c = len(p)
          l = p
    if l != '' and l not in a:
      a.append(l)
    c,l = 0,''
a = sorted(a)
for i in a:
    print(i)
            
            
