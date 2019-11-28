for x in range(int(input())):
    total, score = map(int, input().split())
    list1 = sorted(list(map(int, input().split())))
    score = list1[-score]
    print(total - list1.index(score))
