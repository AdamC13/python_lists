#1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades = sorted(grades, reverse = True)
print(grades)

total = 0
for grade in grades:
    total += grade
total = total / len(grades)
print(total)

i = 0
while i < len(grades):
    if grades[i] < 80:
        grades[i] = "Failed"
    i += 1
print(grades)


#2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#attended = ["Charlie", "Bob", "Alice", "David"]
good_students = []
for student in submitted:
    if student in attended:
        good_students.append(student)
print(good_students)

if len(good_students) == len(submitted) and len(good_students) == len(attended):
    print('The same students submitted and attended')

for student in attended:
    if student not in submitted:
        attended.remove(student)
print(attended)


#3
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week = temperatures[7:14]
print(second_week)

hot_days = []
for temp in temperatures:
    if temp > 100:
        hot_days.append(temp)
print(hot_days)

temperatures.reverse()
print(temperatures[4:10])

#4
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

i = 0
fail = []
failed_students = []
while i < len(grades):
    if grades[i] < 80:
        fail.append(i)
    i += 1
for index in fail:
    failed_students.append(students.pop(index))
    failed_students.append(grades.pop(index))
    failed_students.append(activities.pop(index))
print(failed_students)

students_approved = students
print(students_approved)