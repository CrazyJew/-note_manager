



#Список заголовков
titles = []

#цикл добавления заголовков
title = input("Введите заголовок заметки: ")
titles.append(title)
#Бесконечный цикл добавления заголовков
while True:
    stop_ = input('Добавить еще один заголовок?: Да - Y Нет - N: ')
    if stop_ in ['y', 'Y']: # Условия для добавления заголовков
        title = input("Введите заголовок заметки: ")
        titles.append(title)
    elif stop_ in ['n', 'N']:
        break
    else:
        print("Некоректный ввод, попробуйте снова")
        continue
for i in titles:
    print(f'{i}')