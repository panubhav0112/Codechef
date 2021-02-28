for tc in range(int(input())):
  n = int(input())
  ll = list(map(int,input().split()))
  ll.sort(reverse=True)
  a = float('-inf')
  for i in range(1,n):
    a = max(a,ll[i-1]*ll[i]+ll[i-1]-ll[i])
  print(a)
