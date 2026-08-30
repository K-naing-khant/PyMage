"""
contacts = {
  "Alice": "555-1234",
  "Bob": "555-5678",
  "Carol": "555-9012"
}
print("Contact book:")
for name, number in contacts.items():
  print(f"{name}: {number}")

print(f"\nBob's number: {contacts["Bob"]}")
print(f"Dave's number: {contacts.get("Dave", "Not found")}")
"""

#REPL
"""
person = {'name': "Alex", "age": 25}
print(person["name"])
print(person["age"])
print(person)

person["city"] = "Bangkok"
print(person)

print(f"\n{person.keys()}")
print(person.values())
print(person.items())
"""


#nested dict
'''
students = {
  "Alice": {
    "grade": "A",
    "age": 20
  },
  "Bob": {
    "grade": "B",
    "age": 22
  }
}
print(students["Alice"]["grade"])

for name, info in students.items():
  print(f"{name} is {info["age"]} and got grade {info["grade"]}")
'''


#building dict
"""
squares = {}
for n in range(1, 6):
  squares[n] = n ** 2
print(squares)

#short way
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)
"""
