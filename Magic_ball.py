from random import choice
import time


class MagicBall:
    answers = [
        # Положительные
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Определённо да",
        "Уверен в этом",

        # Нерешительно положительные
        "Мне кажется — «да»",
        "Вероятнее всего",
        "Хорошие перспективы",
        "Знаки говорят — «да»",
        "Да",

        # Нейтральные
        "Пока не ясно, попробуй снова",
        "Спроси позже",
        "Лучше не рассказывать",
        "Сейчас нельзя предсказать",
        "Сконцентрируйся и спроси опять",

        # Отрицательные
        "Даже не думай",
        "Мой ответ — «нет»",
        "По моим данным — «нет»",
        "Перспективы не очень хорошие",
        "Весьма сомнительно"
    ]

    def __init__(self):
        self.answers = self.answers

    def answer(self):
        return choice(self.answers)

    def waiting(self):
        for i in range(1,5):
            print('.')
            time.sleep(1)

    def start(self):
        print(f'{"*" * 7}Предсказатель запущен{"*" * 7}')

        while True:
            while True:
                user_question = input('Задай свой вопрос: ')
                if user_question.endswith('?') or user_question.endswith(' '):
                    print(f'Ваш вопрос:\n{user_question}')
                    break
                else:
                    print('Разве это вопрос ? Вопросы заканчиваются на "?"')

            print(f'{"*" * 7}Мне надо подумать{"*" * 7}')
            self.waiting()
            print(self.answer())

            while True:
                yes_no = input('У вас остались вопросы?: ')
                if yes_no == 'да' or yes_no == 'нет':
                    if yes_no == 'да':
                        break
                    else:
                        print('Рад был помочь ^_^')
                        exit(0)
                else:
                    print('Так да или нет ?')


if __name__ == '__main__':
    game = MagicBall()
    game.start()


