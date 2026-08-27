# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# # print(type(height))

# bmi = weight / (height ** 2)
# print(f'Your BMI is {bmi}')

# is_healthy_range = bmi >= 18.5 and bmi <= 24.9
# print(f"IN healthy BMI range: {is_healthy_range}")


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight/(height**2)
is_healthy_range = bmi >= 18.5 and bmi <= 24.9

print(f"Your weight is {str(weight)} kg, your height is {str(height)} m and your BMI is {bmi}.")
print(f"In healthy BMI range: {is_healthy_range}")