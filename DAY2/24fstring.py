#number manipulation and F string in pyhton
print(int(8/3))
print(round(8/3))
print(round(8/3 , 2)) #here we are writing comman to define the precision of decimal 
#means where we want to place the point 2.67
print(round(8/3 , 4)) #2.6667

#modifying numbers
#instead of division and making round of it 
#we can use floor(8//2) it will give integer as result instead of float.
print(8//3) 
# ouput = 2
print(type(8 //3))
print(type(4/3))

result = 4/2
result /= 2
print(result)

#user score
score = 0

#user scores a point
score += 2
print(score)

score -= 1
print(score)

#F string
# score = 0 
# print("your score is " + score)
# it will throw an error becoz score is int and your score is string
# so making use of F string we can resolve this error instead of doing type conversion or type casting

score = 0 
height = 1.8
isWining = True
#f-string
print(f"your score is {score}, your height is {height}, you are wining is {isWining}")
