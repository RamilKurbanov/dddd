def is_attacking_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            # Проверка на то же самое местоположение или на атаку по строке, столбцу или диагонали
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

# Пример использования:
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

if is_attacking_queens(queens):
    print("Ферзи не бьют друг друга.")
else:
    print("Есть ферзи, которые бьют друг друга.")