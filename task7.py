def mul(operand, operator):
    if operator == 1 or operand == 1:
        return operand
    elif operator == 0 or operand == 0:
        return 0
    else:
        return operand + mul(operand, operator - 1)

while True:
    print(mul(int(input()), int(input())))