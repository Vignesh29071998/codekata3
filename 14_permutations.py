from itertools import permutations
n=list(input())
n1=list(permutations(n))
a=[]
for i in n1:
  if i not in a:
    a.append(i)
    print(''.join(i))
