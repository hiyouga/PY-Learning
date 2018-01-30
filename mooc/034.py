#reverse.py
def reverse(s):
	if s == "":
		return s
	else:
		return reverse(s[1:]) + s[0]
'''
rev(abc)
rev(bc) + a
rev(c) + b + a
c + b + a
cba
'''
print(reverse("Hello")) 