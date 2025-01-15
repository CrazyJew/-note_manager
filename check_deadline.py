from datetime import datetime  # Импорт модуля Datetime

# Вывод сегодняшней даты
date_today = datetime.today()
print("Сегодняшняя дата - ", date_today.strftime('%d-%m-%Y'))
# Цикл получения даты дедлайна и проверки коректности ввода
while True:
    try:
        issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
        cor_issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
        print(f'дедлайн установлен на: ', cor_issue_date.strftime('%d-%m-%Y'))
    except ValueError:
        print("Некоректный ввод, введите дату в нужном формате")
    else:
        break
# проверка сроков дедлайнов

if cor_issue_date.date() == date_today.date():
    print("Сегодня дедлайн!")
elif cor_issue_date > date_today:
    dedline = cor_issue_date - date_today
    print(f'До дедлайна осталось:', dedline)
elif cor_issue_date < date_today:
    dedline = date_today - cor_issue_date
    print(f'Дедлайн прошел:', dedline.days, 'дней назад')
