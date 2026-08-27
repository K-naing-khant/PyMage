score = float(input("Enter your score (0-100): "))

if score >= 90:
  if score == 100:
    print("Perfect score!")
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
  print("Grade F")