n=int(input())
n1=list(map(int,input().split()))
a=''
while len(n1)>0:
  a+=str(max(n1))
  n1.remove(max(n1))
print(a)
