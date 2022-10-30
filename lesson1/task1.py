import numpy as np

# создаем единичную матрицу размерности 10
a = np.eye(10)

# загружаем из txt матрицу размерности 10
b = np.genfromtxt("x.txt", delimiter=' ', dtype=np.float)

# перемножаем 2 матрицы
result = np.linalg.solve(a, b)

# сохраняем результат в таблицу
result.tofile('res.csv',sep=',',format='%10.5f')
