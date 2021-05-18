def validTicTacToe(board):
    b = '|'.join(board)
    x, o = (any(p*3 in b[s::d] for s in range(9) for d in (1, 3, 4, 5)) for p in 'XO')
    m = b.count('X') - b.count('O')
    return m == (not o) if m else not x

def won(l):
    if l[0][0]==l[0][1]==l[0][2]!="_": return True
    if l[1][0]==l[1][1]==l[1][2]!="_": return True
    if l[2][0]==l[2][1]==l[2][2]!="_": return True
    if l[0][0]==l[1][0]==l[2][0]!="_": return True
    if l[0][1]==l[1][1]==l[2][1]!="_": return True
    if l[0][2]==l[1][2]==l[2][2]!="_": return True
    if l[0][0]==l[1][1]==l[2][2]!="_": return True
    if l[0][2]==l[1][1]==l[2][0]!="_": return True
    return False

for _ in range(int(input())):
    l = []
    xc,oc=0,0
    for i in range(3):
        ip = input()
        xc += ip.count('X')
        oc += ip.count('O')
        l.append(ip)
    
    if not validTicTacToe(l):
        print(3)
    elif (xc+oc)<9 and (not won(l)):
        print(2)
    else:
        print(1)