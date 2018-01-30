#addintersert3.py
def addInterest(balances, rate):
	for i in range(len(balances)):
		balances[i] = balances[i] * (1 + rate)
def main():
	amounts = [1000, 105, 3500, 739]
	rate = 0.05
	addInterest(amounts, rate)
	print(amounts)
main()