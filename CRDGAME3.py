from math import ceil
for _ in range(int(input())):
	chef,rick = list(map(int,input().split()))
	cd = ceil(chef/9)
	rd = ceil(rick/9)
	w = 0 if cd<rd else 1
	print(w,min(cd,rd))