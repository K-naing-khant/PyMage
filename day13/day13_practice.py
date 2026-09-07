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
# try:
#   account.withdraw(200)
# except ValueError as e:
#   print(f"Transaction failed: {e}")

##rap a full menu loop with error handling

while True:
  print("\n1. Deposit 2. Withdraw 3. Check Balance 4. Quit")
  choice = input("Choose an option: ")

  if choice == "4":
    break

  try:
    if choice == "1":
      amount = float(input("Amount to deposit: "))
      account.deposit(amount)
    elif choice == "2":
      amount = float(input("Amount to withdraw: "))
      account.withdraw(amount)
    elif choice == "3":
      print(f"Balance: ${account.balance}")
    else:
      print("Invalid choice.")
  except ValueError as e:
    print(f"Error: {e}")