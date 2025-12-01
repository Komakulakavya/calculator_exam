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
a=10
b=50
op='*'
res=calculator(a,b,op)

print("Result:", res)
