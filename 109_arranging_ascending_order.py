n = int(input())
s = list(input().split())
a = []
for i in s:
  a.append(i.lower())
for i in sorted(a):
  print(i)
