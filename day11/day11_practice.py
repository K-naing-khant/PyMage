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

  def check_balance(self):
    print(f"{self.owner}'s current balance: ${self.balance}")

account = BankAccount("Alex", 100)
account.check_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)
account.check_balance()

print(f"\n{account.owner}'s balance: ${account.balance}")