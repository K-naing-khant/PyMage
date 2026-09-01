students = [
  {"name": "Alice", "score": 85},
  {"name": "Bob", "score": 72},
  {"name": "Carol", "score": 91}
]

sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)

for student in sorted_students:
  print(f"{student['name']}: {student['score']}")
