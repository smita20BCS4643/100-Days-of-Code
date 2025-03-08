# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇  
total_height = 0

for heights in student_heights:
  total_height += int(heights)

number_of_students = 0

for lengths in student_heights:
  number_of_students += 1

Average_height = round(total_height / number_of_students)
print(Average_height)
