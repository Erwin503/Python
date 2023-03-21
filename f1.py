import re

def calculate(expression):

    tokens = re.findall(r'[-+*/%()]|\d+', expression)
    for token in tokens:
        print(token, end = '')
    print('')

    operand_stack = []
    operator_stack = []

    def add_operator_to_stack(op):
        while operator_stack and operator_stack[-1] != '(' and precedence(operator_stack[-1]) >= precedence(op):
            operator = operator_stack.pop()
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            result = evaluate_expression(operator, left_operand, right_operand)
            operand_stack.append(result)
        operator_stack.append(op)

    def evaluate_expression(operator, left_operand, right_operand):
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '/':
            return left_operand / right_operand
        elif operator == '%':
            return left_operand % right_operand

    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/' or operator == '%':
            return 2
        else:
            return 0

    for token in tokens:
        if token.isdigit():
            operand_stack.append(int(token))
        elif token in '+-*/%':
            add_operator_to_stack(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                operator = operator_stack.pop()
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
                result = evaluate_expression(operator, left_operand, right_operand)
                operand_stack.append(result)
            operator_stack.pop()

    while operator_stack:
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        result = evaluate_expression(operator, left_operand, right_operand)
        operand_stack.append(result)

    return operand_stack[0]
while True:
    exp =  input('Enter an expression: ')
    print('The result is', calculate(exp))