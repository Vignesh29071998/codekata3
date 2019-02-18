a=int(input())
b=list(input().split())
c=input()
d=len(c)
count=0
for i in range(0,a):
  if b[i][:d]==c:
    count+=1
print(count)
