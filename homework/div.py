import re

line = input()
matchObj = re.match('dividend = (-?\d+), divisor = (-?\d+)', line)

if matchObj:
    a, b = map(int, [matchObj.group(1), matchObj.group(2)])
    if b == 0:
        print("No")
    else:
        print(a//b)
else:
    print("No")
   
