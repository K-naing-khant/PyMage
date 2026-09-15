def create_expense(item, amount):
  return {"item": item, "amount": amount}

def total_expenses(expenses):
  return sum(e["amount"] for e in expenses)