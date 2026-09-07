##normal one
# a = 10
# b = 0
# result = a / b
# print(result)


#try/except/else/finally
a = 10
b = 0
try:
  result = a / b
  print(f"Result: {result}")
except ZeroDivisionError:
  print("Error: cannot divide by zero!")