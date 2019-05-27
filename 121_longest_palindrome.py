s = input()
m = 0
for i in range(0,len(s)-1):
  for j in range(i+1,len(s)):
    p = s[i:j+1]
    if p == p[::-1]:
      if len(p) > m:
        m = len(p)
        c = p
print(c)
