now we will learn about the function in python
def caca():
    print("hello")
    print("welcome to the world of python programming")
caca()
caca()
caca()

def sum(a,b):
    s=a+b
    return s
  print(sum(10,5))
this will print the sum of the 10 and 15 which is 15


def average(a,b,c):
    avg=(a+b+c)/3
    return avg
  
  print(average(2,3,4))
 the output will be an average of the 3 number


def count_value(n):
    count=0
    for i in range(len(str(n))):
        count+=1
        n=n // 10
        
    return count
n=int(input("enter the number"))
print("the value of the count_value is ",count)


THE AUTOMATIC CALCULTOR NY USING THE PYTHON


def calculator(a,b,operator):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        if b != 0:
            return a/b
        else:
            return "division by zero is not allowed"
    else:
          return "invalid operator"

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /) or type 'quit' to stop: ")

    if operator == "quit":
        print("Calculator stopped.")
        break

    result = calculator(a, b, operator)
    print("Result:", result)




the use of the functions for the calculation of the average , grade, AND RESULT

def calculate_total(math, physics, english):
    total = math + physics + english
    return total


def calculate_average(total):
    average = total / 3
    return average


def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Main program

name = input("Enter student name: ")

math = int(input("Enter Math marks: "))
physics = int(input("Enter Physics marks: "))
english = int(input("Enter English marks: "))

total = calculate_total(math, physics, english)

average = calculate_average(total)

grade = calculate_grade(average)

result = check_result(average)

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)
