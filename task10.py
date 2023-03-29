import re
from tkinter import *

def converter():
    line = txt.get()
    phone_regex = r"(?:(?:\+7|8)?[- ]\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}|8?[- ]3652[- ]?\d{2}[- ]?\d{2}[- ]?\d{2}|8?[- ]3652[- ]?\d{3}[- ]?\d{3})"
    result = "Результат:"
    tmp = re.findall(phone_regex, line)
    for i in tmp:
        if i[0] == '8':
            i = "+7" + i[1:]
        i = i.replace(' ', '')
        i = i.replace('-', '')
        result = result + '\n' + i
    lbl.configure(text = result)

window = Tk()
window.title("Number")
window.geometry('1000x700')

txt = Entry(window, width = 100)
txt.grid(column = 0, row = 0)

lbl = Label(window, text = "Результат")
lbl.grid(column = 0, row = 1)

btn = Button(window, text ="Convert", command = converter)
btn.grid(column = 1, row =0)

window.mainloop()
# Это мой номер телефона: +7 123 456-78-90. А это номер моего друга: 8-800-123-45-67. 8 3652-09-67 80 gnbtgbny 8 3652-567 789