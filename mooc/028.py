#bool
'''
a or not b and c
	==
(a or ((not b) and c))
'''
ans = input("What flavor do you want [vanilla]:")
if ans != "":
	flavor = ans
else:
	flavor = "vanilla"
if ans:
	flavor = ans
else:
	flavor = "vanilla" 
flavor = ans or "vanilla"
flavor = input("What flavor do you want [vanilla]:") or "vanilla"