class Account:
	def __init__(self, name, balance, min_balance):
		self.name = name
		self.balance = balance
		self.min_balance = min_balance
	
	def deposit(self, amount):
		self.balance += amount
	
	def withdraw(self, amount):
		if self.balance - amount >= self.min_balance:
			self.balance -= amount
		else:
			print("Sorry, not enought funds!")

	def statement(self):
		print("Account Balance: ${}".format(self.balance))


class Current(Account):
	def __init__(self, name, balance):
		super().__init__(name, balance, min_balance = -1000)
	def __str__(self):
		return"{}'s Current Account: Balance ${}".format(self.name,self.balance)

class Savings(Account):
	def __init__(self, name, balance):
		super().__init__(name, balance, min_balance = 0)
	def __str__(self):
		return"{}'s Savings Account: Balance ${}".format(self.name,self.balance)


x = Current("Vilius", 500)
x.statement()
x.deposit(300)
x.statement()
x.withdraw(1000)
x.statement()
x.withdraw(1000)
print(x)


t=Savings("Tom", 300)

print(t)
t.withdraw(300)
t.statement()
t.withdraw(100)
