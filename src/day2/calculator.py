a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter operator (+ - * /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")
