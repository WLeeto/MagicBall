from tkinter import *
from tkinter import messagebox as mb
from PIL import Image as PilImage
from PIL import ImageTk

from Magic_ball import MagicBall


class MagicBall_widget(MagicBall):
    def __init__(self, width, height, title='Main Window', resizable=(False, False), icon=r'resourses/ico.ico'):
        super().__init__()
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+1100+200')
        # self.root.resizable(resizable[0], resizable[1])

        img = PilImage.open(r"resourses\main_theme.png")
        img = img.resize((200, 200), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        if icon:
            self.root.iconbitmap(icon)

        self.answer = MagicBall()
        self.lable = Label(self.root, text='Задай свой вопрос', font=('Consolas', 20, 'bold'), width=50, height=2)

    def draw_widgets(self):
        self.draw_menu()

        Label(self.root, image=self.photo_image).pack(pady=15)
        self.lable.pack()
        Button(self.root, text='Дай ответ', width=50, height=2, command=self.gimme_answer).pack()
        Button(self.root, text='Exit', width=50, height=2, command=self._exit).pack(pady=15)

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label='Выйти', command=self._exit)

        settings_menu = Menu(menu_bar, tearoff=0)
        connection_menu = Menu(settings_menu, tearoff=0)
        connection_menu.add_command(label='Установить новое соединение')
        connection_menu.add_command(label='Отключить соединение')
        settings_menu.add_cascade(label='Подключения', menu=connection_menu)

        about_menu = Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='О приложении', command=self.show_info)

        menu_bar.add_cascade(label='Фаил', menu=file_menu)
        menu_bar.add_cascade(label='Настройки', menu=settings_menu)
        menu_bar.add_cascade(label='Инфо', menu=about_menu)

        self.root.configure(menu=menu_bar)

    def show_info(self):
        info_name = "Разработчик ООО 'Руки крюки'"
        info = "Данное приложение разработана исключительно для упрощения принятия решений\n" \
               "Скрипт связывается с непостижимыми космическими силами, поэтому будьте осторожны\n\n" \
               "Приложение не предназначено для использование в военных целях"
        mb.showinfo(info_name, info)

    def _exit(self):
        choice = mb.askyesno("Выход", "Действительно хотите выйти ?")
        if choice:
            self.root.destroy()

    def gimme_answer(self):
        answer = self.answer.answer()
        self.lable.configure(text=f'{answer}')

    def run(self):
        self.draw_widgets()
        self.root.mainloop()


if __name__ == "__main__":
    test = MagicBall_widget(450, 440)
    test.run()
