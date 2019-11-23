idstr = input()
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
total = 0
for i in range(17):
    total += weight[i] * int(idstr[i])
verify = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
if str(verify[total % 11]) == idstr[17]:
    print('YES')
else:
    print('NO')
