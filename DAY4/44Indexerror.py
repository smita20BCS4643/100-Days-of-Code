states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
"Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america)

print(len(states_of_america))
#throwing error becoz stats their are 50 states in america but in programing indexing starts from 0 so we have items till 49
#that's y 50 will give error
# print(states_of_america[50])

num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])

#list in list
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
               "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Apples", "Grapes", "Peaches","Cherries","Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes","Celery","Potatoes"]

dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
print(dirty_dozen[1][1])
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
