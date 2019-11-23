import re

gst = input()
print('Yes' if re.match(r'114514-g[a-zA-Z-_]* s[a-zA-Z-_]* t[a-zA-Z-_]*', gst) else 'No')
