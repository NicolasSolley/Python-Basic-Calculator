# My first python calculator build
print()
print("[Python Calculator]")
#Addition, subtraction, multiplication, and division calculator
print()


def calculator():
    num1 = float(input("Enter first number: "))
    op = input("Enter Operation \n[+, -, *, /]: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = (float(num1) + float(num2))
        print(result)
    elif op == "-":
        result = (float(num1) - float(num2))
        print(result)
    elif op == "*":
        result = (float(num1) * float(num2))
        print(result)
    elif op == "/":
        result = (float(num1) / float(num2))
        print(result)
    else:
        print("Please enter a valid operation")
        calculator()
calculator()

