n=int(input())
n1,n2=[],[]
c=0
for i in range(0,n):
  n1.append(list(map(int,input().split())))
for i in range(0,n+2):
  if i==0:
    n2.append([0]*(n+2))
  elif i==(n+2)-1:
    n2.append([0]*(n+2))
  else:
    n2.append([0]+n1[i-1]+[0])
for i in range(0,len(n2)):
  

    
