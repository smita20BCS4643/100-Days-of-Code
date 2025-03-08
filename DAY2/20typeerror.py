#length function doesn't work with integer

num_char = len(input("what's is your name? "))
# print("Your name has" + num_char + "Charaters.")
# output will produce can only concatenate str (not 'int') to string
# how can prevent this error. check the data type making use of type() function
 
print(type(num_char))
#or we can do type conversion or type casting
num_char = len(input("what's is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " Charaters.")
a = 123
print(type(a))

a = float(123)
print(type(a))
print(70 + float("100.5"))
print(str(70)+ str(100))

