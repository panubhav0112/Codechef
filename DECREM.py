for _ in range(int(input())):
	l,r = list(map(int,input().split()))
	if r-l == r%l: print(r)
	else: print(-1) 
