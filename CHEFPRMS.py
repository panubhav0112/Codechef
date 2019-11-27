# ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# sp = []
# leng = len(ls)
# for i in range(leng):
#     for j in range(i + 1, leng):
#         if (ls[i] * ls[j]) < 200:

#             sp.append(ls[i] * ls[j])

# print(sp)


def p(num):
    for i in sp:
        if num - i in sp:
            return True
    return False


sp = set([6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94, 106, 118, 122, 134, 142, 146, 158, 166, 178, 194, 15, 21, 33, 39, 51, 57, 69, 87, 93, 111, 123, 129, 141, 159, 177, 183, 35, 55, 65, 85, 95, 115, 145, 155, 185, 77, 91, 119, 133, 161, 143, 187])

for case in range(int(input())):
    num = int(input())
    if p(num):
        print("YES")
    else:
        print("NO")
