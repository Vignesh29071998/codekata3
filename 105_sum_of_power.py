n = input()
su = 0
for i in range(0,len(n)):
  su += int(n[i])**len(n)
print(su)
