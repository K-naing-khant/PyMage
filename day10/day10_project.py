students = [
  {"name": "Alice", "score": 85},
  {"name": "Bob", "score": 72},
  {"name": "Carol", "score": 91},
  {"name": "Dave", "score": 60}
]

for s in students:
  print(f"{s['name']}: {s['score']}")

# add a function to add new students
def add_student(students, name, score):
  students.append({"name": name, "score": score})
  return students

students = add_student(students, "Eve", 78)
# print(students)

#add a function to assign letter grades (from Day 3 logic)
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for s in students:
    s["grade"] = get_grade(s["score"])

for s in students:
    print(f"{s['name']}: {s['score']} ({s['grade']})")


#sort by score, and filter for each grade
top_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nRanked by score:")
for s in top_students:
    print(f"{s['name']}: {s['score']} ({s['grade']})")

honor_roll = list(filter(lambda s: s["grade"] == "A", students))
print(f"\nHonor roll (A grade): {[s['name'] for s in honor_roll]}")