import re
input()
expression = 'erhvbrt-()nbgrbj1+1'
tokens = re.findall(r'[-+*/%()]|\d+', expression)

print(tokens)