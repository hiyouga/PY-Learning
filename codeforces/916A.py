#916A
def main():
	x = int(input())
	h, m = map(int, input().split())
	h = int(h)
	m = int(m)
	t = 0
	while not checktime(h, m):
		h, m = uptime(h, m, x)
		t += 1
	print(t)

def uptime(h, m, x):
	m -= x
	if m < 0:
		if h == 0:
			h = 23
		else:
			h -= 1
		m += 60
	return h, m

def checktime(h, m):
	return '7' in str(h) or '7' in str(m)

if __name__ == '__main__':
	main()