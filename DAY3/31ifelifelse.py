#rollercoster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    
    print("You Can ride the Rollercoaster!")
    age = int(input("How old are you? "))
    if age >= 12 and age <= 18:
        print("You have to pay $7 to take ride of rollercoster")
    elif age < 12:
        print("You have to pay $3 to take ride of rollercoster")
    else:
        print("You have to pay $12 to take ride of rollercoster")

  
else:
  print("Sorry ,You have to grow taller before You Can ride!")
