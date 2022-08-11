# Окно
from cProfile import label
from main import download_video

import tkinter as tk


def add(name):
        name = name.get()
        print(name)
        download_video(name)
        

win = tk.Tk()
# Окно
win.config() # цвет фона
win.title('YouTube Downloader')
win.geometry("300x70+600+200") # РАзмер окна + где появляется
win.resizable(False, False) # Блокировка размера окна 

# Поля ввода и вывода
tk.Label (win, text = 'Ссылка').grid(row=0, column=0, sticky='w', padx= 5)
entry_name = tk.Entry(width=30)
entry_name.grid(row=0, column=1, sticky='ew')

# кнопки
btn1 = tk.Button(win, text= 'Скачать', command= lambda: add(entry_name)).grid(row=1, column=1, sticky='e', pady = 10)
win.mainloop()

