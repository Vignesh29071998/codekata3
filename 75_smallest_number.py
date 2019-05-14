n = int(input())
li = list(map(int,input().split()))
a = []
for i in range(0,n-1):
  if li[i]>li[i+1]:
    a.append(li[i+1])
  else:
    a.append(-1)
a.append(-1)
print(*a)
