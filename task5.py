def sum(num1, num2):
    return(num1 + num2)
def dif(num1, num2):
    return(num1 - num2)
def mul(num1, num2):
    return(num1 * num2)
def div(num1, num2):
    if num2 == 0:
        return('я отказываюсь такое считать')
    else:
        return(num1 / num2)
while True:
    num1 = int(input())
    sign = input()
    num2 = int(input())
    if sign == '+':
        print(sum(num1, num2))
    if sign == '-':
        print(dif(num1, num2))
    if sign == '*':
        print(mul(num1, num2))
    if sign == '/':
        print(div(num1, num2))