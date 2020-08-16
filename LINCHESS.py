for _ in range(int(input())):
	n,k = list(map(int,input().split()))
	p = list(map(int,input().split()))
	p = [float('inf') if k%n else k//n for n in p]

	ans = min(p)
	if ans==float('inf'):
		print(-1)
	else:
		print(k//ans)
	