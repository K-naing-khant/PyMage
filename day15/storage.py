import csv

def save_expense(expense, filename="expenses.csv"):
  with open(filename, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([expense["item"], expense["amount"]])

def load_expenses(filename="expenses.csv"):
  expenses = []
  with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      item, amount = row
      expenses.append({"item": item, "amount": float(amount)})
  return expenses
