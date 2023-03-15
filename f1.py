import re

def calculate(expression):

    tokens = re.findall(r'[-+*/%()]|\d+', expression)

    operand_stack = []
    operator_stack = []

    def add_operator_to_stack(op):
        # Пока на вершине стека операторов находится оператор с более высоким или равным приоритетом,
        # перемещать операторы из стека операторов в стек операндов и повторять эту операцию.
        while operator_stack and operator_stack[-1] != '(' and precedence(operator_stack[-1]) >= precedence(op):
            operator = operator_stack.pop()
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            result = evaluate_expression(operator, left_operand, right_operand)
            operand_stack.append(result)
        operator_stack.append(op)

    # Определить функцию, которая вычисляет результат для данного оператора и операндов
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

    # Определить функцию, которая возвращает приоритет оператора
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/' or operator == '%':
            return 2
        else:
            return 0

    # Обработать каждый токен в выражении
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

    # Пока в стеке операторов есть операторы, перемещать их в стек операндов и вычислять результат
    while operator_stack:
        operator = operator_stack.pop()
        right_operand = operand_stack.pop()
        left_operand = operand_stack.pop()
        result = evaluate_expression(operator, left_operand, right_operand)
        operand_stack.append(result)

    #