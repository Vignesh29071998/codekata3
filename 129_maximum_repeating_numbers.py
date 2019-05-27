n = int(input())
a = list(map(int,input().split()))
c,b,m = 0,[],0
for i in range(0,n):
    if a[i] not in b:
        b.append(a[i])
        for j in range(i+1,n):
            if a[i] == a[j]:
                c += 1
        if c > m:
            m = c
            p = a[i]
    c = 0
print(p)
            
    
