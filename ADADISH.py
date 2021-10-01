for i in range(int(input())):
  ip = input()
  arr = list(map(int,input().split()))
  sum1,sum2 = 0,0
  for a in sorted(arr,reverse=True):
    if sum1>sum2:
      sum2+=a
    else:
      sum1+=a
  print(max(sum1,sum2))
