n = int(input())
while n > 0:
	print(sum(int(x) for x in input().split()))
	n = n - 1