n=int(input())
n1=list(map(int,input().split()))
for i in range(0,len(n1)-1):
  for j in range(i+1,len(n1)):
    if n1[i]+n1[j]==0:
      print(n1[i],n1[j])
      break
      
