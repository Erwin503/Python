while True:
    str1 = input('Введите задачу: ')
    chars = ['+', '-', '*', '/']
    i = 0
    while i < len(str1):
        if str1[i] in chars:
            num1 = int(str1[:i])
            num2 = int(str1[i+1:])
            char = str1[i]
            print(char)
            break
        i = i + 1
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