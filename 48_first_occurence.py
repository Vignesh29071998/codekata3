s1=input()
s2=input()
for i in range(0,(len(s1)-len(s2))+1):
  if s1[i:i+len(s2)]==s2:
    print(i)
    break
else:
  print('-1')
