n = input()
su = 0
for i in range(0,len(n)):
  for j in range(0,i+1):
    su += int(n[j])
print(su)
