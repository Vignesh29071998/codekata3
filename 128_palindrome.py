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
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if len(a[i])==len(a[j]):
            if a[i][0] > a[j][0]:
                a[i],a[j] = a[j],a[i]
        elif len(a[i]) > len(a[j]):
            a[i],a[j] = a[j],a[i]
for i in a:
    print(i)
            
