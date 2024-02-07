def plus_two(number):
    try:
        result = 2 + int(number)
        print("Результат сложения:", result)
    except ValueError:
        print("Ожидаемый тип данных — число!")

if __name__ == "__main__":
    number = input("Введите число: ")
    plus_two(number)
