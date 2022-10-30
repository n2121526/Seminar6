# Задача 1. Создайте программу для игры в "Крестики-нолики".
new_field = 4

def get_field(new_field):
    array = []
    for i in range(new_field):
        array.append([])
        if i == 0:
            array[i] = [j for j in range(new_field)]
        else:  
            array[i] = ["." for j in range(new_field)]
            array[i][0] = i
    return array

def print_field(field):
    for i in range(new_field):
        for j in range(new_field):
            print(field[i][j], end=" ")
        print()

def check_win():
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2]:
            return True
        if array[0][i] == array[1][i] == array[2][i]:
            return True
    if array[0][0] == array[1][1] == array[2][2]:
        return True
    if array[0][2] == array[1][1] == array[2][0]:
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if array[i][j] != "X" and array[i][j] != "O":
                return False
    return True

def check_input(x, y, new_field):
    if x < 1 or x > new_field - 1:
        return False
    if y < 1 or y > new_field - 1:
        return False
    return True

def make_move(x, y, player):
    array[x][y] = player

def game():
    print("ИГРА Крестики - нолики")
    print("Укажите через пробел номер строки и столбца: ")
    print("Первыми ходят крестики")
    print_field(array)
    player = "X"
    while True:
        print("Ходят крестики" if player == "X" else "Ходят нолики")
        x, y = map(int, input().split())
        if not check_input(x, y, new_field):
            print("Нет такой клетки")
            continue
        if array[x][y] != ".": 
            print("Клетка занята")
            continue
        make_move(x, y, player)
        print_field(array)
        if check_win():
            print("Победили крестики" if player == "X" else "Победили нолики")
            break
        if check_draw():
            print("Ничья")
            break
        player = "X" if player == "O" else "O"

def main():
    global array
    array = get_field(new_field)
    game()

if __name__ == "__main__":
    main()
