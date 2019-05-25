n = int(input())
s = list(input().split())
a = []
for i in s:
  if int(i)==78 or int(i)==1 or int(i)==4:
    a.append('+')
  elif int(i[-2:])==35:
    a.append('-')
  elif int(i[0])==9 and int(i[len(i)-1])==4:
    a.append('*')
  elif int(i[:3])==190:
    a.append('?')
  else:
    a.append('*')
for i in a:
  print(i)
