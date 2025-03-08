# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combination = name1+ name2
lowercase = combination.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
first_digit_of_score = t + r + u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
second_digit_of_score = l + o + v + e

score = int(str(first_digit_of_score)+str(second_digit_of_score))
if score < 10 or score >90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
