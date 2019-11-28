for case in range(int(input())):
    num = int(input())
    arr = list(map(int, input().split()))
    z = 0
    for i in range(1, num):
        if arr[i] < arr[i - 1]:
            z += 1
        if z == 2:
            break
    if (z < 2 and arr[-1] <= arr[0]) or z == 0:
        print('YES')
    else:
        print('NO')
