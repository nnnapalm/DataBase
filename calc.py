# импорт модуля
from tkinter import *
import tkinter as tk
from tkinter import ttk # редактирование для большей читаемости

# создание корневого окна
window = Tk()
# заголовок
window.title("Калькулятор")
# размеры
window.geometry("400x600")
# запрет на изменение размера окна
window.resizable(False, False)
# создание разметки
for c in range(4): window.columnconfigure(index=c, weight=1)
for r in range(4): window.rowconfigure(index=r, weight=1)

# получение введённого текста
def show_message():
    label["text"] = entry.get()

entry = ttk.Entry()
entry.grid(row=0, column=0, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.grid(row=0, column=1, padx=6, pady=6)

label = ttk.Label()
label.grid(row=0, column=2, padx=6, pady=6)

# прописывание характеристик кнопок
# числа
btn1 = ttk.Button(text = "1", font=("Lucida Grange Regular", 20))
btn1.grid(row=1, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn2 = ttk.Button(text="2", font=("Lucida Grange Regular", 20))
btn2.grid(row=1, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn3 = ttk.Button(text="3", font=("Lucida Grange Regular", 20))
btn3.grid(row=1, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn4 = ttk.Button(text="4", font=("Lucida Grange Regular", 20))
btn4.grid(row=2, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn5 = ttk.Button(text="5", font=("Lucida Grange Regular", 20))
btn5.grid(row=2, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn6 = ttk.Button(text="6", font=("Lucida Grange Regular", 20))
btn6.grid(row=2, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn7 = ttk.Button(text="7", font=("Lucida Grange Regular", 20))
btn7.grid(row=3, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn8 = ttk.Button(text="8", font=("Lucida Grange Regular", 20))
btn8.grid(row=3, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn9 = ttk.Button(text="9", font=("Lucida Grange Regular", 20))
btn9.grid(row=3, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn0 = ttk.Button(text="0", font=("Lucida Grange Regular", 20))
btn0.grid(row=4, column=0, ipadx=15, ipady=40, padx=2, pady=2)
# точка
btndot = ttk.Button(text=".", font=("Lucida Grange Regular", 20))
btndot.grid(row=4, column=1, ipadx=20, ipady=40, padx=4, pady=2)
# операции
btnplus = ttk.Button(text="+", font=("Lucida Grange Regular", 20))
btnplus.grid(row=1, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnmin = ttk.Button(text="–", font=("Lucida Grange Regular", 20))
btnmin.grid(row=2, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnmultiply = ttk.Button(text="*", font=("Lucida Grange Regular", 20))
btnmultiply.grid(row=3, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnsection = ttk.Button(text="/", font=("Lucida Grange Regular", 20))
btnsection.grid(row=4, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnequals = ttk.Button(text="=", font=("Lucida Grange Regular", 20))
btnequals.grid(row=4, column=2, ipadx=15, ipady=40, padx=2, pady=2)

# запуск бесконечного цикла
window.mainloop()