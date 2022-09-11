from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk
from tkinter import messagebox

from Magic_ball import MagicBall


class MagicBall_widget(MagicBall):
    def __init__(self, width, height, title='Main Window', resizable=(False, False), icon=r'resourses/ico.ico'):
        super().__init__()
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+1200+200')
        # self.root.resizable(resizable[0], resizable[1])

        img = PilImage.open(r"resourses\main_theme.png")
        img = img.resize((200, 200), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        if icon:
            self.root.iconbitmap(icon)

        self.answer = MagicBall()
        self.lable = Label(self.root, text='Задай свой вопрос',font=('Consolas', 20, 'bold'), width=50, height=2)

        self.empty_lable = Label(self.root, width=50, height=2)

    def draw_widgets(self):
        Label(self.root, image=self.photo_image).pack(pady=15)
        self.lable.pack()
        Button(self.root, text='Дай ответ', width=50, height=2, command=self.gimme_answer).pack()
        self.empty_lable.pack()
        Button(self.root, text='Exit', width=50, height=2, command=self.exit).pack()

    def exit(self):
        choice = messagebox.askyesno("Выход", "Действительно хотите выйти ?")
        if choice:
            self.root.destroy()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def gimme_answer(self):
        answer = self.answer.answer()
        self.lable.configure(text=f'{answer}')


if __name__ == "__main__":
    test = MagicBall_widget(450, 440)
    test.run()

