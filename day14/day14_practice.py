import csv

def add_expense(item, amount):
  with open("my_expenses.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([item, amount])

add_expense("Coffee", 4.50)

while True:
  print("\n1. Add expense  2. View expenses  3. Quit")
  choice = input("Choose: ")

  if choice == "3":
    break
  elif choice == "1":
    item = input("Item: ")
    try:
      amount = float(input("Amount: "))
      add_expense(item, amount)
      print("Saved!")
    except ValueError:
      print("Invalid amount.")
  elif choice == "2":
    pass #build this in Stage 3

def view_expenses():
  total = 0
  with open("my_expenses.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
      item, amount = row
      amount = float(amount)
      total += amount
      print(f"{item}: ${amount:.2f}")
  print(f"Total: ${total:.2f}")