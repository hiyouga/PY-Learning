#dic.py
stu = {"203-2012-045":"John", "203-2012-037":"Peter"}
stu["202-2011-121"] = "Susan"
print(stu["202-2011-121"])
del stu["202-2011-121"]

for key in stu:
	print(key+" : "+str(stu[key]))
for value in stu.values():
	print(value)
for item in stu.items():
	print(item)

print("203-2012-037" in stu)

print(tuple(stu.keys()))
print(tuple(stu.values()))
print(tuple(stu.items()))

print(stu.get("203-2012-045"))
print(stu.pop("203-2012-045"))

print(stu)

stu.clear()

print(stu)