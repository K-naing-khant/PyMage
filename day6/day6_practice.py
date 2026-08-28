shopping_list = ["milk", "eggs", "bread"]
# print(shopping_list)

new_item = input("Enter an item to add: ")
shopping_list.append(new_item)
# print(f"Update list: {shopping_list}")

remove_item = input("Enter an item to remove: ")
if remove_item in shopping_list:
  shopping_list.remove(remove_item)
  print(f"Removed {remove_item}")
else:
  print(f"{remove_item} wasn't on the list.")
print(f"Updated list: {shopping_list}")

print("\nFinal shopping list:")
for index, item in enumerate(shopping_list, start=1):
  print(f"{index}. {item}")