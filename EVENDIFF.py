for _ in range(int(input())):
  n = int(input())
  ll = list(map(int,input().split()))
  o = len([_ for _ in ll if _&1])
  print(min(o,n-o))
