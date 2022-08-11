from cProfile import label
from email import message
from view import show, add_contact

import tkinter as tk


def say():
    print('123')

def del_list(lb):
    lb.delete(0, 'end')
    lb.insert('end', *show())

def del_list2():
    lb.delete(0, 'end')  

def win2():
    def add(f, n, t, w):
        f = f.get()
        n = n.get()
        t = t.get()
        add_contact([f, n, t,])
        w.destroy()
    
    win2 = tk.Tk()
    win2.title('Добавить контакт')
    win2.geometry("300x130+600+150") # РАзмер окна + где появляется
    win2.resizable(False, False) # Блокировка размера окна 
    tk.Label (win2, text = 'Фамилия').grid(row=0, column=0, sticky='w')
    tk.Label (win2, text = 'Имя').grid(row=1, column=0, sticky='w')
    tk.Label (win2, text = 'Телефон').grid(row=2, column=0, sticky='w')
    entry_f = tk.Entry(win2)
    entry_f.grid(row=0, column=1)
    entry_n = tk.Entry(win2)
    entry_n.grid(row=1, column=1)
    entry_t = tk.Entry(win2)
    entry_t.grid(row=2, column=1)
    btn = tk.Button(win2, text= 'Добавить', command= lambda: add(entry_f, entry_n, entry_t, win2)).grid(row=3, column=1, sticky='e')


win = tk.Tk()

# Окно
win.config(bg= '#B7A3A3') # цвет фона
win.title('Телефонный справочник')
win.geometry("500x400+600+200") # РАзмер окна + где появляется
win.resizable(False, False) # Блокировка размера окна 

# Поля ввода и вывода
name = tk.Entry(width=30).grid(row=0, column=1, sticky='ew',padx =10)

# text = tk.Text(width=30, height=10)
# text.grid(row=3, column=1, rowspan=2, padx =10)
lb = tk.Listbox(width=30, height=10)
lb.grid(row=3, column=1, rowspan=2, padx =10)


# кнопки

btn1 = tk.Button(win, text= 'Поиск', command= say).grid(row=0, column=0, sticky='e', pady = 10)
btn2 = tk.Button(win, text= 'Добавить контакт', command= win2).grid(row=1, column=0, sticky='ew')
btn3 = tk.Button(win, text= 'Показать список', command= lambda: del_list(lb)).grid(row=3, column=0, sticky='new')
btn4 = tk.Button(win, text= 'Очистить список', command= lambda: lb.delete(0, 'end')).grid(row=4, column=0, sticky='w') # перестала работать


win.mainloop()




