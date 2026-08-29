class_a = ["Alice", "Bob", "Carol", "Dave"]
class_b = ["Carol", "Dave", "Eve", "Frank"]
print(f"Class A: {class_a}")
print(f"Class B: {class_b}")

set_a = set(class_a)
set_b = set(class_b)
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

in_both = set_a & set_b
print(f"\nStudents in both classes: {in_both}")

only_in_a = set_a - set_b
only_in_b = set_b - set_a
print(f"Only in Class A: {only_in_a}")
print(f"Only in Class B: {only_in_b}")

counts = (len(in_both)), len(only_in_a), len(only_in_b)
both_count, a_count, b_count = counts
print(f"\n{both_count} shared, {a_count} only in A, {b_count} only in B")