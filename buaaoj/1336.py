def dest(t, d):
	#print(d)
	if d == 0:
		return 1
	s = 0
	for i in range(1, min(d, t)+1):
		s += dest(i, d-i)
	return s

n = int(input())
print(dest(n, n))