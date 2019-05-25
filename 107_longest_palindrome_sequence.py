s = input()
c = 1
for i in range(0,len(s)):
  for j in range(i+1,len(s)):
    s1 = s[i:j]
    if s1 == s1[::-1]:
      m = len(s1)
    if m > c:
      c = m
print(c)
