for _ in range(int(input())):

  def solve():
    c = int(input())*0
    s = input()
    for i in s:
      if i=='1':
        c+=1
      else:
        c-=1
      if c>=0:
        return "YES"
    return "NO"
  
  print(solve())
