#916B
n, k = map(int, input().split())
b = n
t = -1
while b > 0:
	b >>= 1
	t += 1
print(1<<t)
for i in range(64, -64, -1):
	