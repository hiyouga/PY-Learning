import re
line = input()
print("True" if re.match(r'(^\d{5}$)|(^((ZY)|(SY)|(BY))\d{7}$)|(^\d{8}$)', line) else "False")
