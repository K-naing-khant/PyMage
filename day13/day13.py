def safe_divide(a, b):
  try:
    result = a / b
    print(f"Result: {result}")
  except ZeroDivisionError:
    print("Error: cannot divide by zero!")

safe_divide(10, 2)
safe_divide(10, 0)

try:
  age = int(input("Enter your age: "))
  print(f"You are {age} years old.")
except ValueError:
  print("Error: that's not a valid number!")