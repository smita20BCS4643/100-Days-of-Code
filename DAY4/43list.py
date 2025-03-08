#list looks pretty simple set of square brakets many items stored inside
#items can be float, integer, boolean (mix datatypes)
#syntax = starting with open square brakets and each item seperated by comma
#list is order
#list is mutable

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
"Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#print the first element or item of list
#beacause indexing start from 0 
print(states_of_america[0])

#we can print negative index also
#it will print last element or item of list
print(states_of_america[-1])

#we can change items of list
print(states_of_america[1])
states_of_america[1] = "pencilvania"
print(states_of_america[1])

#we can add items in the last of list
#append is used to add item at the end of the list
states_of_america.append("smita")
print(states_of_america)

#we can add another items into preexisting list
#extend is used 
states_of_america.extend(["smita", "aku", "saku"])
print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
