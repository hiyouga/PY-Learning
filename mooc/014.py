#pm25.py

def main():
	pm = eval(input("What is today?"))
	if pm > 75:
		print("Unhealthy")
	if pm < 35:
		print("Good")

main()

print(3 < 4)
print(3 * 4 < 3 + 4)
print("hello" == "hello")
print("abc" < "def")
print("abc" > "def")