def find(i, str1):
    num1 = ''
    num2 = ''
    start = 0
    end = 0
    operators = ['+', '-', '*', '%', '/']
    for j in range(i - 1, -1, -1):
        if str1[j] not in operators:
            num1 = num1 + str1[j]
            start = j
        else:
            break
    for j in range(i + 1, len(str1)):
        if str1[j] not in operators:
            num2 = num2 + str1[j]
            end = j
        else:
            break
    num1 = num1[::-1]

    if str1[i] == '+':
        str1 = str1[:start:] + str(int(num1) + int(num2)) + str1[end+1:]
    elif str1[i] == '-':
        str1 = str1[:start:] + str(int(num1) - int(num2)) + str1[end+1:]
    elif str1[i] == '*':
        str1 = str1[:start:] + str(int(num1) * int(num2)) + str1[end+1:]   
    elif str1[i] == '/':
        str1 = str1[:start:] + str(int(num1) / int(num2)) + str1[end+1:]    
    elif str1[i] == '%':
        str1 = str1[:start:] + str(int(num1) % int(num2)) + str1[end+1:]
    return(str1)
    


def calculate(str1):
    operators = ['+', '-', '*', '%', '/']
    isReady = True
    for i in range(len(str1) - 1):
        if str1[i] in operators:
            isReady = False
            break
    if isReady:
        return str1
    else:
        for i in range(len(str1)):
            if str1[i] == ')':
                for j in range(i - 1, 0 , -1):
                    if str1[j] == '(':
                        str1 = str1[:j] + calculate(str1[j+1:i])
        for i in range(len(str1) - 1):
            if str1[i] == '*' or str1[i] == '/' or str1[i] == '%':
                    str1 = find(i, str1)
        for i in range(len(str1)):
            if str1[i] in operators:
                str1 = find(i, str1)
            for i in range(len(str1) - 1):
                if str1[i] in operators:
                    isReady = False
                    break
                if isReady:
                    return str1
                else: 
                    return calculate(str1)
    

while True:
    str1 = input('Введите задачу: ')
    arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '%', '/', '(', ')']
    i = 0
    while i < len(str1):
        if str1[i] not in arr:
            str1 = str1[:i] + str1[i+1:]
        else:
            i = i + 1
    print(str1)
    arrF = [ '*', '%', '/']
    if str1[0] in arrF:
        print('Invalid input')
    else:
        print(calculate(str1))