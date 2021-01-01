def xyz():
  n,k,x,y = list(map(int,input().split()))  
  k=(k-1)%4
  dx = n-x
  dy = n-y
  mn = min(dx,dy)
  x,y = x+mn,y+mn
  
  if(x==y):
    print(n,n)
    return

  for i in range(k):
    if not i&1:
      x,y = y,x
    else:
      mn = min(x,y)
      x,y = x-mn,y-mn

  print(x,y)

for _ in range(int(input())):
  xyz()
