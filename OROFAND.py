for _ in range(int(input())):
  n,queries = list(map(int,input().split()))
  arr = list(map(int,input().split()))
  bc = [0]*31

  for a in arr:
    for i in range(31):
      num = 1<<i
      if a&num > 0:
        bc[i]+=1

  ans = 0
  for i in range(31):
    num = 1<<i
    if bc[i]>0: ans+=num
  print(ans)
  
  for q in range(queries):
    ind,val = list(map(int,input().split()))
    old = arr[ind-1]
    arr[ind-1] = val
    ans = 0
    for i in range(31):
      num = 1<<i
      if old&num > 0:
        bc[i]-=1
      if val&num > 0:
        bc[i]+=1
      if bc[i]>0:
        ans+=num
    print(ans)
  
