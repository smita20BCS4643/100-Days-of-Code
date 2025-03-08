# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_weight = int(weight)
new_height = float(height)

BMI = new_weight / (new_height * new_height)
result = round(BMI)
print(result)
