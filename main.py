from tkinter import *
from tkinter import ttk
import requests
from io import  BytesIO

window = Tk()
window.title('Какая ты булочка?')

# задан размер окна и параметры отображения(посередине экрана)
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
width_position = screenwidth // 2 - 300
height_position = screenheight // 2 - 300
window.geometry(f'600x600+{width_position}+{height_position}')

window.mainloop()