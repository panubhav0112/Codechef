def xyz(arr1,arr2,n,m):
  n = min(n,m)
  diff = sum(arr2)-sum(arr1)
  if diff<0:
    return 0
  for i in range(n):
    diff-= 2*(arr2[i] - arr1[i])
    if diff<0:
      return i+1
  return -1

for _ in range(int(input())):
  n,m = list(map(int,input().split()))
  arr1 = list(map(int,input().split()))
  arr2 = list(map(int,input().split()))
  arr1.sort()
  arr2.sort(reverse=True)
  print(xyz(arr1,arr2,n,m))
