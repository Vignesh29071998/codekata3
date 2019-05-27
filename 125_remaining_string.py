s = input()
s1,a,c = '',{},1
for i in range(0,len(s)):
  if s[i] not in a:
    if i != len(s)-1:
      for j in range(i+1,len(s)):
        if s[i] == s[j]:
          c += 1
      a[s[i]] = c
      c = 1
    else:
      a[s[i]] = c
for i in a:
  if a[i] == 1:
    s1 += i
print(s1)
