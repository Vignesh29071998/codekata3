from itertools import permutations
n=input()
a=[]
l=list(permutations(list(n)))
for i in l:
  a.append(''.join(i))
a=sorted(a)
for i in a:
  if n<i:
    print(i)
    break
else:
  print('impossible')
