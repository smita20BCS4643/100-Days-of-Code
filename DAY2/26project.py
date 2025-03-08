#Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#Greetings
print("Welcome to the tip calculator!")

#Input for the bill
bill = float(input("What was the total bill? $"))

#Input for the tip
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))

#Input for how many peoples are splitting the bill
split = int(input("How many people to split the bill? "))

#calculating bill with tip
bill_with_tip = tip / 100 * bill + bill 

#calculating bill after adding tip and splitting into persons
bill_per_person = bill_with_tip/split

#formating the result upto 2 decimal places.
final_amount = "{:.2f}".format(round(bill_per_person,2))

#printing the finall result.
print(f"Each person should pay: ${final_amount}")
