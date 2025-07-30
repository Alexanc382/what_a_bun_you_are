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
width_position = screenwidth // 2 - 200
height_position = screenheight // 2 - 230
window.geometry(f'400x460+{width_position}+{height_position}')


label_0 = ttk.Label(text='Выбери один вариант ответа в каждом вопросе:')
label_0.grid(row=0, column=0 , columnspan=2) # приветствие, описание для пользователя

# метка 1-го вопроса
label_1 = ttk.Label(text=f'{que.question_1}')
label_1.grid(row=1, column=0, columnspan=2, sticky='w', padx=(5, 0))

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_1_1}')
rad_butt_1_1.grid(row=2, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_1_2}')
rad_butt_1_2.grid(row=3, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_1_3}')
rad_butt_1_3.grid(row=4, column=0, columnspan=2, sticky='w', padx=(10, 0))

# метка 2-го вопроса
label_2  = ttk.Label(text=f'{que.question_2}')
label_2.grid(row=5, column=0, columnspan=2, sticky='w', padx=(5, 0))

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_2_1}')
rad_butt_1_1.grid(row=6, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_2_2}')
rad_butt_1_2.grid(row=7, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_2_3}')
rad_butt_1_3.grid(row=8, column=0, columnspan=2, sticky='w', padx=(10, 0))

# метка 3-го вопроса
label_3  = ttk.Label(text=f'{que.question_3}')
label_3.grid(row=9, column=0, columnspan=2, sticky='w', padx=(5, 0))

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_3_1}')
rad_butt_1_1.grid(row=10, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_3_2}')
rad_butt_1_2.grid(row=11, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_3_3}')
rad_butt_1_3.grid(row=12, column=0, columnspan=2, sticky='w', padx=(10, 0))

# метка 4-го вопроса
label_4 = ttk.Label(text=f'{que.question_4}')
label_4.grid(row=13, column=0, columnspan=2, sticky='w', padx=(5, 0))

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_4_1}')
rad_butt_1_1.grid(row=14, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_4_2}')
rad_butt_1_2.grid(row=15, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_4_3}')
rad_butt_1_3.grid(row=16, column=0, columnspan=2, sticky='w', padx=(10, 0))

# метка 5-го вопроса
label_5 = ttk.Label(text=f'{que.question_5}')
label_5.grid(row=17, column=0, columnspan=2, sticky='w', padx=(5, 0))

rad_butt_1_1 = ttk.Radiobutton(text=f'{que.answer_5_1}')
rad_butt_1_1.grid(row=18, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_2 = ttk.Radiobutton(text=f'{que.answer_5_2}')
rad_butt_1_2.grid(row=19, column=0, columnspan=2, sticky='w', padx=(10, 0))
rad_butt_1_3 = ttk.Radiobutton(text=f'{que.answer_5_3}')
rad_butt_1_3.grid(row=20, column=0, columnspan=2, sticky='w', padx=(10, 0))


#прогрессбар загрузки
progress_bar = ttk.Progressbar(mode="determinate", length=300)
progress_bar.grid(row=21, column=0, sticky='w', padx=(5, 0))
# кнопка для обработки результатов ответов пользователя
button_send = ttk.Button(text='Отправить')
button_send.grid(row=21, column=1, sticky='e', padx=(0, 5))

window.mainloop()