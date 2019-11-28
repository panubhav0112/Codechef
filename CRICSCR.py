runs = 0
wickets = 0
n = int(input())


def val_scr():
    global runs, wickets, n
    for i in range(n):
        xruns, xwickets = map(int, input().split())
        if xruns < runs or xwickets > 10 or xwickets < wickets or (wickets == 10 and xwickets):
            return "NO"
        runs = xruns
        wickets = xwickets
    return "YES"


print(val_scr())
