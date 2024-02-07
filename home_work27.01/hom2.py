try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Введите индекс элемента массива: "))
    value = my_list[index]
    print("Значение элемента массива:", value)

except IndexError:
    print("Ошибка: Индекс выходит за границы массива")
except ValueError:
    print("Ошибка: Введите целое число в качестве индекса")
