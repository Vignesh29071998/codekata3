n,k=map(int,input().split())
n1=list(map(int,input().split()))
i=0
while i<len(n1):
  if n1[i]==k:
    del n1[i]
  else:
    i+=1
if n1==[]:
  print('empty')
else:
  print(*n1)
