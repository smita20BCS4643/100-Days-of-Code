# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight /(height ** 2 ))
print(BMI)

# Under 18.5 they are underweight
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
# Over 18.5 but below 25 they have a normal weight 
elif BMI >= 18.5 and BMI <= 25:
  print(f"Your BMI is {BMI}, you are normal weight.")
# Over 25 but below 30 they are slightly overweight  
elif BMI >= 25 and BMI <= 30:
  print(f"Your BMI is {BMI}, you are slightly weight.")
# Over 30 but below 35 they are obese
elif BMI >= 30 and BMI <= 35:
  print(f"Your BMI is {BMI}, you are obese.")
# Above 35 they are clinically obese. 
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
