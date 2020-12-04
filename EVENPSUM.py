from math import ceil,floor

for _ in range(int(input())):
  n1,n2 = list(map(int,input().split()))
  en1 = floor(n1/2)
  on1 = ceil(n1/2)
  en2 = floor(n2/2)
  on2 = ceil(n2/2)
  print((en1*en2)+(on1*on2))
