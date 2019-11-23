dic = [
    ["","I","II","III","IV","V","VI","VII","VIII","IX"],
    ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
    ["","M","MM","MMM"]
    ]
num = int(input())
res = ''
res += dic[3][num // 1000 % 10]
res += dic[2][num // 100 % 10]
res += dic[1][num // 10 % 10]
res += dic[0][num % 10]
print(res)
