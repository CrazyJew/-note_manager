

# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

temp_created_date = list(created_date)
temp_issue_date = list(issue_date)

# Выводим введенные данные
print("Вы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", *temp_created_date[0:5])
print("Дата истечения заметки:", *temp_issue_date[0:5])
