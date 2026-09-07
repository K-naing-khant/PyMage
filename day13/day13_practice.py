class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive.")
    self.balance += amount
    print(f"Deposited ${amount}. New balance: ${self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      raise ValueError("Insufficient funds!")
    self.balance -= amount
    print(f"Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("Alex", 100)
try:
  account.withdraw(200)
except ValueError as e:
  print(f"Transaction failed: {e}")