"""
todo_list = ["Buy groceries", "Walk the dog", "Finish homework"]

print("Your to-do list:")
for item in todo_list:
  print(f'- {item}')

todo_list.append("Read a book")
print(f"\nAdded a task. Now: {todo_list}")

todo_list.remove("Walk the dog")
print(f"Removed a task. Now: {todo_list}")

print(f"\nTotal task: {len(todo_list)}")
"""


#Long way (Day 4 style)
square = []
for n in range(1, 6):
  square.append(n ** 2)
print(square)

# Short way - list comprehension
square = [n ** 2 for n in range(1, 6)]
print(square)

evens = [n for n in range(1, 6) if n % 2 == 0]
print(evens)