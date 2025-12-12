# импорт модуля
from tkinter import *
import tkinter as ttk

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
for r in range(5): window.rowconfigure(index=r, weight=1)

# отображение информации в главной строке
entry = ttk.Entry(window, justify=ttk.RIGHT, font=("Lucida Grange Regular", 20))
entry.insert(0, '')
entry.grid(row=0, column=0, columnspan=3, padx=5)

# внесение изменений в главную строку
def add_digit(digit):
    value = entry.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    entry.delete(0, ttk.END)
    entry.insert(0, value + digit)

# выполнение операций
def add_operation(operation):
    value = entry.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = entry.get()
    entry.delete(0, ttk.END)
    entry.insert(0, value + operation)

# обработка событий c последним знаком операции
def calculate():
    value = entry.get()
    if value[-1] in '+-/*':
        value = value + value[:-1]
    entry.delete(0, ttk.END)
    entry.insert(0, eval(value))

# отображение введённых значений в строку entry
def ent0():
    entry.insert(END, "0")
def ent1():
    entry.insert(END, "1")
def ent2():
    entry.insert(END, "2")
def ent3():
    entry.insert(END, "3")
def ent4():
    entry.insert(END, "4")
def ent5():
    entry.insert(END, "5")
def ent6():
    entry.insert(END, "6")
def ent7():
    entry.insert(END, "7")
def ent8():
    entry.insert(END, "8")
def ent9():
    entry.insert(END, "9")
def summ():
    entry.insert(END, "+")
def minn():
    entry.insert(END, "-")
def mull():
    entry.insert(END, "*")
def sect():
    entry.insert(END, "/")
def dott():
    entry.insert(END, ".")


# прописывание характеристик кнопок чисел
# числа
btn1 = ttk.Button(text = "1", font=("Lucida Grange Regular", 20), command=ent1)
btn1.grid(row=1, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn2 = ttk.Button(text="2", font=("Lucida Grange Regular", 20), command=ent2)
btn2.grid(row=1, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn3 = ttk.Button(text="3", font=("Lucida Grange Regular", 20), command=ent3)
btn3.grid(row=1, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn4 = ttk.Button(text="4", font=("Lucida Grange Regular", 20), command=ent4)
btn4.grid(row=2, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn5 = ttk.Button(text="5", font=("Lucida Grange Regular", 20), command=ent5)
btn5.grid(row=2, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn6 = ttk.Button(text="6", font=("Lucida Grange Regular", 20), command=ent6)
btn6.grid(row=2, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn7 = ttk.Button(text="7", font=("Lucida Grange Regular", 20), command=ent7)
btn7.grid(row=3, column=0, ipadx=15, ipady=40, padx=2, pady=2)
btn8 = ttk.Button(text="8", font=("Lucida Grange Regular", 20), command=ent8)
btn8.grid(row=3, column=1, ipadx=15, ipady=40, padx=2, pady=2)
btn9 = ttk.Button(text="9", font=("Lucida Grange Regular", 20), command=ent9)
btn9.grid(row=3, column=2, ipadx=15, ipady=40, padx=2, pady=2)
btn0 = ttk.Button(text="0", font=("Lucida Grange Regular", 20), command=ent0)
btn0.grid(row=4, column=0, ipadx=15, ipady=40, padx=2, pady=2)
# точка
btndot = ttk.Button(text=".", font=("Lucida Grange Regular", 20), command=dott)
btndot.grid(row=4, column=1, ipadx=15, ipady=40, padx=2, pady=2)
# операции
btnplus = ttk.Button(text="+", font=("Lucida Grange Regular", 20), command=summ)
btnplus.grid(row=1, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnmin = ttk.Button(text="–", font=("Lucida Grange Regular", 20), command=minn)
btnmin.grid(row=2, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnmultiply = ttk.Button(text="*", font=("Lucida Grange Regular", 20), command=mull)
btnmultiply.grid(row=3, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnsection = ttk.Button(text="/", font=("Lucida Grange Regular", 20), command=sect)
btnsection.grid(row=4, column=3, ipadx=15, ipady=40, padx=2, pady=2)
btnequals = ttk.Button(text="=", font=("Lucida Grange Regular", 20), command=calculate)
btnequals.grid(row=4, column=2, ipadx=15, ipady=40, padx=2, pady=2)

# запуск бесконечного цикла
window.mainloop()