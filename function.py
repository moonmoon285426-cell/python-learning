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
