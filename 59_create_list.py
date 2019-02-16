n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[a[i]+b[i] for i in range(0,n)]
print(*c)
