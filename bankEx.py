class BankInfo:

	def __init__(self, accountType, checkingAmount, savingsAmount):
		self.accountType = accountType
		self.checkingAmount = checkingAmount
		self.savingsAmount = savingsAmount
	
	def deposit(self, accountType, amountIn):
		if (accountType.lower() == "checking".lower()):
		  self.checkingAmount += amountIn
		  print("${} deposited in your {}".format(amountIn, accountType))
		elif (accountType.lower() == "savings".lower()):
		  self.savingsAmount += amountIn
		  print("${} deposited in your {}".format(amountIn, accountType))
		else:
		  print ("Error: choose 'checking' or 'savings' as account type")
		
	def withdraw(self, accountType, amountOut):
		if (accountType.lower() == "checking".lower()):
		  self.checkingAmount -= amountOut
		  print("${} withdrawn from your {}".format(amountOut, accountType))
		elif (accountType.lower() == "savings".lower()):
		  self.savingsAmount -= amountOut
		  print("${} withdrawn from your {}".format(amountOut, accountType))
		else:
		  print ("Error: choose 'checking' or 'savings' as account type")

myAccount = BankInfo("Savings", 100, 500)

myAccount.deposit("c", 20) # this tests if my error message works
myAccount.withdraw("CHeCking", 30) # test to see if .lower() works
myAccount.deposit("savings", 50)
myAccount.withdraw("savings", 30)

		