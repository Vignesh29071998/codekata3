s,k=input().split()
a=[]
for i in range(0,(len(s)-int(k))+1):
  a.append(s[i:i+int(k)])
print(*a)
