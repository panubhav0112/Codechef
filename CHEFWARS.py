for i in range(int(input())):
	a,b = list(map(int,input().split()))
	while b>0:
		a,b=a-b,b//2
		# print(a,b)
		if a<=0:
			print(0)
			break
	else:
		print(1)