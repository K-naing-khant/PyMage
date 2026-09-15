from models import create_expense, total_expenses
from storage import save_expense, load_expenses

expense = create_expense("Lunch", 12.00)
save_expense(expense)

all_expenses = load_expenses()
print("All expenses:")
for e in all_expenses:
  print(f"{e["item"]}: ${e['amount']:.2f}")

print(f"\nTotal spent: ${total_expenses(all_expenses):.2f}")

while True:
  print("\n1. Add expense 2. View + total 3. Quit")
  choice = input("Choose: ")

  if choice == "3":
    break
  elif choice == "1":
    item = input("Item: ")
    try:
      amount = float(input("Amount: "))
      save_expense(create_expense(item, amount))
      print("Saved!")
    except ValueError:
      print("Invalid amount.")
  elif choice == "2":
    all_expenses = load_expenses()
    for e in all_expenses:
      print(f"{e['item']}: ${e['amount']:.2f}")
    print(f"Total: ${total_expenses(all_expenses):.2f}")