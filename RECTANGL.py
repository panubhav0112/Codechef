for z in range(int(input())):
    x = sorted(list(map(int, input().split())))
    if x[::2] == x[1::2]:
        print("YES")
    else:
        print("NO")
