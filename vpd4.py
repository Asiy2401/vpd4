def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        x_1 = max(x1, x3)
        x_2 = min(x2, x4)
        y_1 = min(y1, y3)
        y_2 = max(y2, y4)
        width = abs(x_1 - x_2)
        height = abs(y_1 - y_2)
        s = width * height
        return s
    except ValueError:
        return -1  # Возвращаем -1 в случае ошибки


def union(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        s_inter = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
        if s_inter > 0:
            s_all = (abs(x1 - x2) * abs(y1 - y2) + (abs(x3 - x4) * abs(y3 - y4))) - s_inter
        else:
            s_all = abs(x1 - x2) * abs(y1 - y2) + abs(x3 - x4) * abs(y3 - y4)
        return s_all
    except ValueError:
        return -1  # Возвращаем -1 в случае ошибки


def main():
    try:
        x1 = int(input("Введите значение оси x левой верхней точки первого прямоугольника: "))
        y1 = int(input("Введите значение оси y левой верхней точки первого прямоугольника: "))
        x2 = int(input("Введите значение оси x правой нижней точки первого прямоугольника: "))
        y2 = int(input("Введите значение оси y правой нижней точки первого прямоугольника: "))
        x3 = int(input("Введите значение оси x левой верхней точки второго прямоугольника: "))
        y3 = int(input("Введите значение оси y левой верхней точки второго прямоугольника: "))
        x4 = int(input("Введите значение оси x правой нижней точки второго прямоугольника: "))
        y4 = int(input("Введите значение оси y правой нижней точки второго прямоугольника: "))
        choice = int(input("Выберите операцию (1 - Площадь пересечения, 2 - Площадь объединения): "))

        if choice == 1:
            s = intersection(x1, y1, x2, y2, x3, y3, x4, y4)
            print("Площадь пересечения:", s if s >= 0 else "Ошибка ввода")
        elif choice == 2:
            s_all = union(x1, y1, x2, y2, x3, y3, x4, y4)
            print("Площадь объединения:", s_all if s_all >= 0 else "Ошибка ввода")
        else:
            print("Ошибка: Неверный выбор операции")
    except ValueError:
        print("Ошибка: Неверный формат ввода")


if __name__ == "__main__":
    main()
    ''''fsdgsdgsdfgsd'''