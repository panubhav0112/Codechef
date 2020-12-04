from math import ceil

for _ in range(int(input())):
  n,d = list(map(int,input().split()))
  arr = list(map(int,input().split()))
  risk,notrisk = 0,0
  for a in arr:
    if a>=80 or a<=9:
      risk+=1
    else:
      notrisk+=1
  days = ceil(risk/d) + ceil(notrisk/d)
  print(days)
