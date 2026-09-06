class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance}")
  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds!")
    else:
      self.balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.balance}")

##Interest_Rate
class SavingAccount(BankAccount):
  def __init__(self, owner, balance=0, interest_rate=0.02):
    super().__init__(owner, balance)
    self.interest_rate = interest_rate

  def apply_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")
savings = SavingAccount("Alex", 1000)
print(savings.apply_interest())

##withdraw()
class CheckingAccount(BankAccount):
  def __init__(self, owner, balance=0, fee=1.5):
    super().__init__(owner, balance)
    self.fee = fee

  def withdraw(self, amount):
    total = amount + self.fee
    if total > self.balance:
      print("Insufficient funds (including fee)!")
    else:
      self.balance -= total
      print(f"Withdrew ${amount} + ${self.fee} fee. New balance: ${self.balance:.2f}")
checking = CheckingAccount("Alex", 100)
print(checking.withdraw(50))

##polymorphism check: loop over mixed accounts types
accounts = [SavingAccount("Sam", 500), CheckingAccount("Jamie", 200)]
for acc in accounts:
  acc.withdraw(50)