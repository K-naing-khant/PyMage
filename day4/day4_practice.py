"""
for number in range(2, 100):
  # print(number)
  is_prime = True
  for divisor in range(2, number):
    if number % divisor == 0:
      is_prime = False
      break
  if is_prime:
      print(number)
"""

'''
for number in range(2, 100):
  # print(number)
  is_prime = True
  for divisor in range(2, number):
    if number % divisor == 0:
      is_prime = False
      break
  if is_prime:
    print(number)
'''


for number in range(2, 100):
  # print(number)
  is_prime = True
  for divisor in range(2, number):
    if number % divisor == 0:
      is_prime = False
      break
  if is_prime:
    print(number)
