from collections import Counter

for _ in range(int(input())):
  n,w,wr = list(map(int,input().split()))
  wa = list(map(int,input().split()))
  c = Counter(wa)
  s = 0
  for i in c:
    if c[i]%2==0:
      s+= i*c[i]
  if s+wr >= w:
    print("YES")
  else:
    print("NO")
