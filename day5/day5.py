'''
password = "Hello123"

length_ok = len(password) >= 8
# print(length_ok)
has_upper = password != password.lower()
has_digit = any(char.isdigit() for char in password)
print(has_digit)

if length_ok and has_upper and has_digit:
  print("Password Strength: STRONG")
else:
  print("Password Strength: WEAK")
'''
