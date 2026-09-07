# try:
#   x = 10 / 2
# except ZeroDivisionError:
#   print("failed")
# else:
#   print("succeeded, no error occurred")
# finally:
#   print("This always runs, error or not")



# print(int("abc"))
# print([1, 2, 3][10])
# print({"a": 1}["b"])
# print(10/0)
"""
ValueError: invalid literal for int() with base 10: 'abc'
IndexError: list index out of range
KeyError: 'b'
ZeroDivisionError: division by zero
"""


try:
  value = int(input("Enter a number: "))
  print(10 / value)
except (ValueError, ZeroDivisionError) as e:
  print(f"Something went wrong: {e}")