n=int(input())
n1=list(map(int,input().split()))
li=[0]*10
for i in range(0,n):
  li[n1[i]]+=1
for i in range(0,len(li)):
  if li[i]==1:
    print(i)
