n=int(input())
n1=[1000,500,100,50,10,1]
c=0
while n>0:
  for i in range(0,len(n1)):
    if n>=n1[i]:
      n=n-n1[i]
      c+=1
      break
print(c)
