#hello
n=int(input())
n1=list(input().split())
a={}
flag=0
for i in range(0,len(n1)-1):
  for j in range(i+1,len(n1)):
    if n1[i]==n1[j] and n1[i] not in a:
      a[n1[i]]=len(n1[i:j+1])
for i in a:
  if a[i]==1:
    flag=0
  else:
    flag=1
    break
if flag==0:
  print('unique')
else:
  print(min(a,key=a.get))
    
       
  

