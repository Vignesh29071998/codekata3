n = int(input())
m = list(map(int,input().split()))
i = 0
while i < len(m):
  if len(m)%2!=0:
    ind = len(m)//2
    print(m[ind])
    m = m[:ind]+m[ind+1:]
  else:
    ind = len(m)//2
    print((m[ind-1]+m[ind])//2)
    m = m[:ind-1]+m[ind+1:]
