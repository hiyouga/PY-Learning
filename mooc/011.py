#list.py

a = [0,1,2,3,4,5,6,7,8,9]
print(a)
print(a[3])
b = [233, "hello", 5.9]
c = a + b
d = a * 2
print(c[10])
print(len(d[2:]))
for i in c:
	print(i)
print("hello" in b)
a.append(10)
e = [5,3,1,8,1,0,-5,6]
e.sort()
print(e)
a.reverse()
print(a)
print(a.index(7))
a.insert(3,-5)
print(d.count(9))
b.remove("hello")
print(b)
c.pop(6)
print(c)
print("python is an excellent language".split())