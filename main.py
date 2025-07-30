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


label_0 = ttk.Label(text='hi')
label_0.pack() # приветствие, описание для пользователя
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()
# метка 1-го вопроса
label_1 = ttk.Label(text='1')
label_1.pack()
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()
# метка 2-го вопроса
label_2  = ttk.Label(text='2')
label_2.pack()
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()
# метка 3-го вопроса
label_3  = ttk.Label(text='3')
label_3.pack()
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()
# метка 4-го вопроса
label_4 = ttk.Label(text='4')
label_4.pack()
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()
# метка 5-го вопроса
label_5 = ttk.Label(text='5')
label_5.pack()
ttk.Radiobutton(text="1 вариант").pack()
ttk.Radiobutton(text="2 вариант").pack()
ttk.Radiobutton(text="3 вариант").pack()

#прогрессбар загрузки
progress_bar = ttk.Progressbar(mode="determinate", length=300)
progress_bar.pack()
# кнопка для обработки результатов ответов пользователя
button_send = ttk.Button(text='Отправить')
button_send.pack()

window.mainloop()