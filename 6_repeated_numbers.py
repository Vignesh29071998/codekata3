n=int(input())
n1=list(input().split())
a={}
for i in range(0,len(n1)-1):
  for j in range(i+1,len(n1)):
    if n1[i]==n1[j] and n1[i] not in a:
      a[n1[i]]=len(n1[i:j+1])
      break
print(min(a,key=a.get))
    
       
