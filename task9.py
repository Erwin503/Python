test = open("test.txt", "r")
res = 0
while True:
    line = test.readline()
    if line:
        res += 1
        print(line, end="")
    else:
        print()
        break
print(res)