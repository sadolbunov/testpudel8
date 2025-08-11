from tkinter import *
import random

window = Tk()
window.title("Кріб")
window.geometry('300x300')

def change_frame_color():
    new_color = random.choice(cveta)
    frame1.config(bg=new_color)


cveta = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#800080"]

frame1 = Frame(window, bg='green', bd=5)
frame2 = Frame(window, bg='blue', bd=5)

button1 = Button(frame1, text="Поміняти колір", command=change_frame_color)

frame1.pack(pady=20)
frame2.pack(pady=20)
button1.pack(pady=100)

window.mainloop()
