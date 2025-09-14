# Take 2 inputs as number 

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

# Take another input as operator + - * /

operator = input("Enter operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("invalid opeator")
