s=input()
if len(s)%2==0:
  s1,s2=s[:len(s)//2],s[len(s)//2:]
  if s1==s2:
    print('YES')
  else:
    print('NO')
else:
  s1,s2=s[:len(s)//2],s[(len(s)//2)+1:]
  if s1==s2:
    print('YES')
  else:
    print('NO')
