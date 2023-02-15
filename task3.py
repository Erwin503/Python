while True:
    str = input('Введите задачу в формате "первое число" "оператор" "второе число": :')
    arr = str.split(' ')
    num1 = int(arr[0])
    num2 = int(arr[2])
    char = arr[1]
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