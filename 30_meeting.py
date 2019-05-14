n = int(input())
a = []
s = list(map(int,input().split()))
e = list(map(int,input().split()))
for i in range(n):
  a.append(abs(s[i]-e[i]))
print(len(a)-1)
