


status_dict = {"1" : "Выполнено", "2" : "Отложено", "3" : "В процессе"}
print(*status_dict.items())

while True:
    status = input("Выберите статус заметки из предложенных выше нажав соотвествующию цифру: ")
    print(f'Ваш выбор:  {status}')
    if status in ['1', '2', '3']:
        status = status_dict.get(status)
        print(f"Статус заметки обновлен: {status}")
        break
    else:
        print('Некорректный выбор. Попробуйте еще раз')
        print(*status_dict.items())
        continue

print(status)
