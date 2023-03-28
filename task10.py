import re
from tkinter import *

def converter():
    line = txt.get()
    phone_regex = r"(?:\+7|8)?[- ](?:(?:\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}))"
    result = "Результат:"
    tmp = re.findall(phone_regex, line)
    for i in tmp:
        result = result + ' ' + i
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
# Это мой номер телефона: +7 123 456-78-90. А это номер моего друга: 8-800-123-45-67.