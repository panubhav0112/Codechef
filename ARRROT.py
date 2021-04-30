M = 10**9+7
_ = input()
s = sum(list(map(int,input().split())))
n = int(input())
_ = input()
for i in range(n):
  s = (s*2)%M
  print(s)
