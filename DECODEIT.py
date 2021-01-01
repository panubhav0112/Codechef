for _ in range(int(input())):
  n = int(input())
  s = input()
  for i in range(0,n,4):
    x = int(s[i:i+4],base=2)
    c = ord('a') + x
    print(chr(c),end="")
  print()
