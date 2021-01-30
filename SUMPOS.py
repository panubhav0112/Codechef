for _ in range(int(input())):
  x,y,z = list(map(int,input().split()))
  if x==y+z or y==x+z or z==x+y:
    print("YES")
  else:
    print("NO")
