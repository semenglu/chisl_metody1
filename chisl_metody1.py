import numpy as np


def gauss_elimination(A, b):
    n = len(A)

    for i in range(n):
        # Находим максимальный элемент во всей матрице, начиная с (i, i)-го элемента
        max_el = abs(A[i][i])
        max_row = i
        for j in range(i, n):
            for k in range(i, n):
                if abs(A[j][k]) > max_el:
                    max_el = abs(A[j][k])
                    max_row = j
                    i = k

        # Меняем строки местами, чтобы максимальный элемент был на диагонали
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Приводим все элементы под диагональю к нулю
        for j in range(i + 1, n):
            c = -A[j][i] / A[i][i]
            for k in range(i + 1, n):
                A[j][k] += c * A[i][k]
            b[j] += c * b[i]
            A[j][i] = 0

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= A[j][i] * x[i]
            A[j][i] = 0

    return x

# Считываем данные из файла
data = np.loadtxt("input.txt")

# Извлекаем матрицу A и вектор-столбец b из данных
A = data[:, :-1]
b = data[:, -1]

# Вызываем функцию для решения системы уравнений
x = gauss_elimination(A, b)

# Выводим решение
print("Solution:")
print(x)