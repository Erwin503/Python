while True:
    num1 = int(input('Введите первое число: '))
    char = input('Введите оператор: ')
    num2 = int(input('Введите второе число: '))
    if char == '+':
        print(num1 + num2)
    elif char == '-':
        print(num1 - num2)
    elif char == '*':
        print(num1 * num2)
    elif char == '/' and num2 != 0:
        print(num1 / num2)
    else:
        print('Error: Invalid character')
