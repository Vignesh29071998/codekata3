s = input()
s1,a = '',[]
for i in range(0,len(s)):
  if s[i] not in a:
    for j in range(i+1,len(s)):
      if s[i] == s[j]:
        a.append(s[i])
        break
    else:
      s1 += s[i]
print(s1)

    


    
