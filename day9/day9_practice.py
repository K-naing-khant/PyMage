#Simple calculator

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Error: cannot divide by zero"
  return a / b

# print(add(2, 3))
# print(divide(10, 0))

while True:
  print("\n1. Add 2. Subtract 3. Multiply 4. Divide 5. Quit")
  choice = input("Choose an option(Only Type number): ")

  if choice == "5":
    print("Goodbye!")
    break

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if choice == "1":
    print(f"Result: {add(num1, num2)}")
  elif choice == "2":
    print(f"Result: {subtract(num1, num2)}")
  elif choice == "3":
    print(f"Result: {multiply(num1, num2)}")
  elif choice == "4":
    print(f"Result: {divide(num1, num2)}")
  else:
    print("Invalid choice, try again.")