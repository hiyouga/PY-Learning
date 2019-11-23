def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return 'N'
    return 'Y'


n = int(input())
if n == 0 or n == 1:
    print('N')
else:
    print(is_prime(n))

