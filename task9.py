test = open("test.txt", "r")
res = 0
dot = 0
com = 0
vosk = 0
quest = 0
while True:
    line = test.readline()
    if line:
        res += 1
        for i in line:
            if i == '.':
                dot += 1
            elif i == ',':
                com += 1
            elif i == '!':
                vosk += 1
            elif i == '?':
                quest += 1 
        
    else:
        break
print("Строк всего: ", res)
print("Точек всего: ", dot)
print("Запятых всего: ", com)
print("Восклицательных знаков всего: ", vosk)
print("Вопросительных знаков всего: ", quest)

test.close()