n=int(input())
n1=list(map(int,input().split()))
for i in range(n-1,-1,-1):
  if i!=0:
    print(n1[i],end='->')
  else:
    print(n1[i])
  
