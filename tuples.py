TUPLE ARE LIKE THE LIST WE USE [] IN THE LIST AND () THIS ONE IN THE LIST
age=(1,2,3,4,5,6)
print(age)

SIMILARLY WE CAN ALSO DO SLICING IN IT
print(age[:3]


       THE IUSE OF THE LOOP ON THE TUPLES
  age=(1,2,3,4,5,6)
for i in age:
      print(i)



THE USE OF TEH LOOP AND ALSO THE F STREAM STRING 
age=(1,2,3,4,5)
sum=0
for i in age:
      sum+=i
print(f"sum of the value is the is {sum}")


WE CAN ALSO PRINT IT BY USE OF TEH INDEX

print(age[0])

  
students = (
    ("Muneeb", 20, "AI", (85, 90, 78, 92, 88)),
    ("Ali", 21, "AI", (72, 65, 80, 75, 70)),
    ("Ahmed", 20, "CS", (95, 88, 91, 89, 94)),
    ("Hamza", 22, "SE", (60, 72, 68, 75, 70))
)


# Function to calculate total marks
def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


# Function to calculate average
def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)

    return average


# Function to calculate grade
def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        return "F"



 A LARGE CODE FOR EERYTHING UNDRSTANDING
# Display all students
print("===== UNIVERSITY STUDENT REPORT =====")

for student in students:

    name = student[0]
    age = student[1]
    program = student[2]
    marks = student[3]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nStudent:", name)
    print("Age:", age)
    print("Program:", program)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


# Find highest marks
print("\n===== HIGHEST MARKS =====")

highest = 0
highest_student = ""

for student in students:

    name = student[0]
    marks = student[3]

    total = calculate_total(marks)

    if total > highest:
        highest = total
        highest_student = name

print("Highest total:", highest)
print("Student:", highest_student)


# Find lowest marks
print("\n===== LOWEST MARKS =====")

lowest = calculate_total(students[0][3])
lowest_student = students[0][0]

for student in students:

    name = student[0]
    marks = student[3]

    total = calculate_total(marks)

    if total < lowest:
        lowest = total
        lowest_student = name

print("Lowest total:", lowest)
print("Student:", lowest_student)


# Find students studying AI
print("\n===== AI STUDENTS =====")

for student in students:

    name = student[0]
    program = student[2]

    if program == "AI":
        print(name)


# Find students who scored more than 80 average
print("\n===== STUDENTS WITH AVERAGE ABOVE 80 =====")

for student in students:

    name = student[0]
    marks = student[3]

    average = calculate_average(marks)

    if average > 80:
        print(name, "->", average)


# Display first three marks of every student
print("\n===== FIRST THREE MARKS =====")

for student in students:

    name = student[0]
    marks = student[3]

    first_three = marks[:3]

    print(name, ":", first_three)


# Display marks in reverse
print("\n===== REVERSE MARKS =====")

for student in students:

    name = student[0]
    marks = student[3]

    reverse_marks = marks[::-1]

    print(name, ":", reverse_marks)


# Check whether a student got 95
print("\n===== CHECK FOR 95 MARKS =====")

for student in students:

    name = student[0]
    marks = student[3]

    if 95 in marks:
        print(name, "got 95 marks")


# Find maximum and minimum marks for each student
print("\n===== MAXIMUM AND MINIMUM MARKS =====")

for student in students:

    name = student[0]
    marks = student[3]

    highest_mark = max(marks)
    lowest_mark = min(marks)

    print(name)
    print("Highest:", highest_mark)
    print("Lowest:", lowest_mark)


# Count how many students are in each program
print("\n===== PROGRAM COUNT =====")

ai_count = 0
cs_count = 0
se_count = 0

for student in students:

    program = student[2]

    if program == "AI":
        ai_count = ai_count + 1

    elif program == "CS":
        cs_count = cs_count + 1

    elif program == "SE":
        se_count = se_count + 1


print("AI students:", ai_count)
print("CS students:", cs_count)
print("SE students:", se_count)




