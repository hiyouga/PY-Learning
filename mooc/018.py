#try2.py

def main():
	try:
		num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
		res = num1 / num2
	except ZeroDivisionError:
		print("Division by zero!")
	except SyntaxError:
		print("A comma may be missing in the input")
	except:
		print("Something wrong in the input")
	else:
		print("No exceptions, the result is", res)
	finally:
		print("executing the final clause")

main()