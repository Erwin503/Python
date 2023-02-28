
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
    return[str1, end - 1]
    
input()
str1 = '9+6*6+8'
HIoperators = ['*', '%', '/']
LOoperators = ['+', '-']
isReady = False
tmp = []
length = len(str1)

# for i in range(len(str1)):
#     if str1[i] == ')':
    #     for j in range(i, 0, -1):
    #         if str[j] == '()':
    #             str1 = str1[:j] + calculate(j, str1) + str1[i:]
for a in range(length):
    if str1[a] in HIoperators:
        tmp = find(a, str1)
        str1 = tmp[0]
        a = tmp[1]
        print(str1)
        length = len(str1) - 1
for a in range(length):
    if str1[a] in LOoperators:
        tmp = find(a, str1)
        str1 = tmp[0]
        a = tmp[1]
        print(str1)
        length = len(str1) - 1
print(str1)