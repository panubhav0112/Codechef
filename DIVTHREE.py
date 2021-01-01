for _ in range(int(input())):
  n,k,d = list(map(int,input().split()))
  s = sum(list(map(int,input().split())))
  print(min(s//k,d))
