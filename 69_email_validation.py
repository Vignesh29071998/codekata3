import collections
s=input()
b={}
if s[-4:]=='.com':
  b=collections.Counter(s)
  if b['@']!=1 or b['@']!=0 and b['.']!=1:
    print('NO')
  else:
    id1=s.index('@')
    id2=s.index('.')
    if len(s[id1+1:id2])>5:
      print('NO')
    else:
      if len(s[:id1])<2:
        print('NO')
      else:
        print('YES')
else:
  print('NO')
