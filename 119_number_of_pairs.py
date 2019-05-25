a = int(input())
b = list(map(int,input().split()))
c = 0
for i in range(0,len(b)-1):
  for j in range(i+1,len(b)):
    if b[i] < b[j]:
      c += 1
print(c)
