def pos(list1, list2, num):
    for i in range(num):
        add = list2[i] - list1[i]
        list1[i] += 1 * add
        list1[i + 1] += 2 * add
        list1[i + 2] += 3 * add

    if list1 == list2:
        return 'TAK'
    else:
        return 'NIE'


for case in range(int(input())):
    num = int(input()) - 2
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(pos(list1, list2, num))
