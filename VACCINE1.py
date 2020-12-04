d1,n1,d2,n2,target = list(map(int,input().split()))
i = 1
while 1:
  if i>=d1:
    target-=n1
  if i>=d2:
    target-=n2
  if target<=0:
    print(i)
    break
  i+=1
