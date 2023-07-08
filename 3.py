# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

def is_attacked(row, col, queens):
    for i in range(row):
        if queens[i] == col or queens[i] - col == i - row or queens[i] - col == row - i:
            return True
    return False

def generate_random_placement(size):
    queens_placement = []
    for row in range(size):
        col = random.randint(0, size-1)
        queens_placement.append(col)
    return queens_placement

def generate_valid_placement(size):
    queens_placement = generate_random_placement(size)
    while True:
        if not is_attacked(size, size-1, queens_placement):
            yield queens_placement
        queens_placement = generate_random_placement(size)

if __name__ == "__main__":
    size = 8
    valid_placement_generator = generate_valid_placement(size)
    successful_placements = []

    while len(successful_placements) < 4:
        queens_placement = next(valid_placement_generator)
        successful_placements.append(queens_placement)
        print(queens_placement)


