for case in range(int(input())):
  l = int(input())
  nums = list(map(int,input().split()))
  ans=0
  for i in range(l):
    for j in range(i+1,l):
      if nums[i]&nums[j] == nums[i]:
        ans+=1
  print(ans)
