from tkinter import *
from tkinter import ttk
import requests
from io import  BytesIO
import questions as que

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

# метка 1-го вопроса
label_1 = ttk.Label(text=f'{que.question_1}')
label_1.pack(pady=8)

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_1_1}')
rad_butt_1_1.pack()
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_1_2}')
rad_butt_1_2.pack()
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_1_3}')
rad_butt_1_3.pack()

# метка 2-го вопроса
label_2  = ttk.Label(text=f'{que.question_2}')
label_2.pack(pady=8)

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_2_1}')
rad_butt_1_1.pack()
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_2_2}')
rad_butt_1_2.pack()
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_2_3}')
rad_butt_1_3.pack()

# метка 3-го вопроса
label_3  = ttk.Label(text=f'{que.question_3}')
label_3.pack()

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_3_1}')
rad_butt_1_1.pack()
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_3_2}')
rad_butt_1_2.pack()
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_3_3}')
rad_butt_1_3.pack()

# метка 4-го вопроса
label_4 = ttk.Label(text=f'{que.question_4}')
label_4.pack(pady=8)

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_4_1}')
rad_butt_1_1.pack()
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_4_2}')
rad_butt_1_2.pack()
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_4_3}')
rad_butt_1_3.pack()

# метка 5-го вопроса
label_5 = ttk.Label(text=f'{que.question_5}')
label_5.pack(pady=8)

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_5_1}')
rad_butt_1_1.pack()
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_5_2}')
rad_butt_1_2.pack()
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_5_3}')
rad_butt_1_3.pack()


#прогрессбар загрузки
progress_bar = ttk.Progressbar(mode="determinate", length=300)
progress_bar.pack()
# кнопка для обработки результатов ответов пользователя
button_send = ttk.Button(text='Отправить')
button_send.pack()

window.mainloop()