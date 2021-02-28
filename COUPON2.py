import math
for _ in range(int(input())):
    d,c=map(int,input().strip().split())
    a1,a2,a3=map(int,input().strip().split())
    b1,b2,b3=map(int,input().strip().split())
    cupon=0
    if((a1+a2+a3)>=150):
        cupon+=(a1+a2+a3)
    else:
        cupon+=a1+a2+a3+d

    if((b1+b2+b3)>=150):
        cupon+=b1+b2+b3
    else:
        cupon+=b1+b2+b3+d

    w=(a1+a2+a3+b1+b2+b3+d+d)
    

    if(cupon+c<w):
        print("YES")
    elif(cupon+c==w):
        print("NO")
    else:
        print("NO")
