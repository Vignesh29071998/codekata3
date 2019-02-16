#hello 
a=list(input())
s=''
i=0
while i<len(a):
  if a[i]==' ':
    s+=a[i]
    for j in range(i+1,len(a)):
      if a[j]==' ':
        i=j+1
      else:
        break
  else:
    s+=a[i]
    i+=1
print(s)
        
        
      
  
