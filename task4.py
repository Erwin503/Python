while True:
    str = input('Введите задачу в формате "первое число" "оператор" "второе число": :')
    arr = str.split(' ')





    # if char == '+':
    #     print(num1 + num2)
    # elif char == '-':
    #     print(num1 - num2)
    # elif char == '*':
    #     print(num1 * num2)
    # elif char == '/' and num2 != 0:
    #     print(num1 / num2)
    # else:
    #     print('Error: Invalid character')
    def calculate(arr):
        l = len(arr)
        for i in arr:
            if arr[i] == '(':
                for j in range(l, i):
                    if arr[j] == ')':
                        calculate(arr[i+1:j-1])
        for i in arr:
            if arr[i] == '*' or arr[i] == '/':
                