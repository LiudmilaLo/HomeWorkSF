print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~Поиграем в Крестики-Нолики??~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ПРАВИЛА ИГРЫ:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Два игрока (№1 и №2) по очереди ставят на свободные клетки поля 3×3 знаки х и о.")
print("Победит тот, кто первым поставит в ряд 3 своих значка по вертикали, горизонтали")
print("или диагонали. Игрок №1 ходит за x, а №2 - за o.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

player1 = (input("Игрок №1, введи свое имя: "))
player2 = (input("Игрок №2, введи свое имя: "))

field = [["-"] * 3 for i in range(3)]


def field_show():
    print(f"   0  1  2")
    for i in range(3):
        print(f"{i}  {field[i][0]}  {field[i][1]}  {field[i][2]} ")


print("Вот наше поле для игры:")
field_show()
print("А теперь потренируемся правильно писать координаты:")


def move():
    while True:
        coordinates = input("Ход! Напиши координаты: ").split()

        if len(coordinates) != 2:
            print("Координаты должны быть в виде двух чисел через пробел. ")
            continue

        x, y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print("Буквенное обозначение недопустимо, введи два числа: ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Нельзя играть вне поля, выбери корректный диапазон от 0 до 2: ")
            continue

        if field[x][y] != "-":
            print("Место занято, выбери другую клетку для хода.")
            continue

        return x, y


move()


def win_ch():
    win_position = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    )

    for position in win_position:
        mark = []
        for i in position:
            mark.append(field[i[0]][i[1]])

        if mark == ['x', 'x', 'x']:
            field_show()
            print("Победа игрока №1! Поздравляю тебя,", player1, ":) !!!")
            return True

        if mark == ['o', 'o', 'o']:
            field_show()
            print("Победа игрока №2! Поздравляю тебя,", player2, ":) !!!")
            return True
    return False


move_order = 0
while True:
    move_order += 1

    field_show()

    if move_order % 2 == 1:
        print(player1, ", твой черёд!")
    else:
        print(player2, ", твой ход!")

    x, y = move()

    if move_order % 2 == 1:
        field[x][y] = "x"
    else:
        field[x][y] = "o"

    if win_ch():
        break

    if move_order == 6:
        print("Давай поднажми!")

    if move_order == 9:
        print("Победила дружба!")
        break
