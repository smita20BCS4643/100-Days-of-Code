#For loop with Range
#used to create range of number
for number in range(1,10):
    print(number)
    #print till 9 last element will not printed
    #by default is increased by 1

#if want to increase by any other number we have to add step size after last range item in declareation
for number in range(1,10,2):
    print(number)
add = 0
for number in range(1, 101):
    add += number
print(add)
