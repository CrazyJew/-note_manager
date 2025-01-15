
from datetime import datetime
import sys

list_notes = []


# функция создания заметки
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


# функция вывода всех заметок
def f_print_notes():
    if list_notes:
        for note in list_notes:
            print(f'Заметка пользователя {note.get("username")}:')
            for key, value in note.items():
                print(f'{key}: {value}')
            print('-' * 20)
    else:
        print("Нет заметок для отображения.")


# функция удаления заметки
def f_delete_note():
    f_print_notes()
    del_note = input('Введите "Имя пользователя" или "Заголовок" заметки, которую хотите удалить: ')

    for note in list_notes:
        if note['username'] == del_note or note['title'] == del_note:
            list_notes.remove(note)
            print(f'Заметка с {del_note} удалена.')
            return
    print("Заметка не найдена!")


# Главный код
while True:
    print(
        'Добро пожаловать в менеджер заметок: \n1. Ваши заметки \n2. Добавить заметку \n3. Удалить заметку \n4. Выход')
    choice = input('Выберите цифру для продолжения: ')
    if choice == '1':
        f_print_notes()
    elif choice == '2':
        list_notes.append(f_add_new_notes())
    elif choice == '3':
        f_delete_note()
    elif choice == '4':
        sys.exit(0)
    else:
        print('Некорректный ввод, повторите попытку.')