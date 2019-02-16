a=input()
if len(a)%2==0:
  i,j=len(a)//2,len(a)//2
  while i>1:
      b,c=a[:i-1],a[j+1:]
      if b==c[::-1]:
        print('YES')
        break
      else:
        i-=1
        j+=1
  else:
      print('NO')
else:
  i,j=len(a)//2,len(a)//2
  while i>0:
    b,c=a[:i],a[j+1:]
    if b==c[::-1]:
      print('YES')
      break
    else:
      i-=1
      j+=1
  else:
    print('NO')
      
      
    
        
