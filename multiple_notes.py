
from datetime import datetime # Импорт модуля Datetime
import sys


#функция создания заметки
def f_add_new_notes():
    note = {}
    note['username'] = input("Введите имя пользователя: ")
    note['title'] = input("Введите заголовок заметки: ")
    note['content'] = input("Введите описание заметки: ")
    note['status'] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
    note['created_date'] = datetime.today()
    while True:
        try:
            issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
            parsed_issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
        except ValueError:
            print("Некоректный ввод, введите дату в нужном формате")
        else:
            break
    note['issue_date'] = parsed_issue_date
    return note
# функция вывода заметки
def f_print_note (note):
    print(f'{note.get("username")}:')
    for key, value in note.items():
        print(f'{key}: {value}')


# Создаем список заметок
list_notes = []
i = True #Флаг приветственного сообщения
#цикл добавления заметок
while True:
    if i == True:
        print('Добро пожаловать в менеджер заметок')
        i = False
    choise = input('Хотите создать новую заметку?' 'yes/no: ').lower()
    if choise in ['y', 'yes']:
        list_notes.append(f_add_new_notes())
        continue
    elif choise in ['n', 'no']:
        if len(list_notes) < 1:
            continue
        else:
            print('\nВаши заметки:')
            for note in list_notes:
                f_print_note(note)
            sys.exit(2)