def calculator(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Invalid operation"
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operation: ")
res=calculator(a,b,op)
print("Result:", res)