for _ in range(int(input())):
    n,k = list(map(int,input().split()))
    x = list(map(int,input().split()))
    print(1 if sum(x)%k else 0)
