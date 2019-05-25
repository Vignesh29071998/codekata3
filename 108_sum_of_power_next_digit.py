n = input()
su = 0
for i in range(0,len(n)):
  if i!=len(n)-1:
    su += int(n[i])**int(n[i+1])
  else:
    su += int(n[i])**int(n[0])
print(su)
