n = int(input())
def fact(n):
  if n == 0:
    return 1
  else:
    return n*fact(n-1)
if n <= 2:
  print(n)
else:
  print((n+(fact(n)//(fact(n-2)*fact(2))))//2)
