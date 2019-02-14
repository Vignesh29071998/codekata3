a,b=list(map(int,input().split()))
l=[[abs(i-b),i] for i in list(map(int,input().split(" ")))]
l.sort()
l=l[1:]
c=[i[1] for i in l[:3]]
print(*c)
