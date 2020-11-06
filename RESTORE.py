for i in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  ans = [None]*n
  for a in range(n-1,-1,-1):
    ans[a] = 1000001 - (n-arr[a])
  
  print(' '.join([str(_) for _ in ans]))
