


#словарь для храниния заметок
note = {}
# запрос данных у пользователя заметки, которые сразу полу
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note["created_date"] = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
#цикл добавления заголовков заметки
note["titles"] = []
for a in range(3):
    title = input(f"Введите заголовок заметки: {a + 1},")
    note["titles"].append(title)
#Вывод данных
for key, value in note.items():
    print(f"{key}, {value}")

