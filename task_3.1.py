# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:

    def __init__(self, rows = 0, columns = 0) -> None:
        '''констркутор с параметрами - размерность матрицы, количество строк, количество столбцов'''
        print(f'Создаем матрицу размером {rows} x {columns}')
        self.data = []
        for rowNum in range(0, rows):
            aRow = []
            for colNum in range(0, columns ):
                aRow.append(1)
            self.data.append(aRow)

    def showSize(self):
        '''выести размер матрицы'''
        if self.data != None:
            print('Размер матрицы: ', len(self.data) , 'x' , len(self.data[0]))
        else:
            print('матрица пуста')

    def updateCell(self, row_num, col_num, new_value):
        '''Изменить ячейку с указанным номером строки и столбца'''
        if self.data == None:
            print('невозможно изменить значение - матрица пуста')
            return
        if row_num > len(self.data) or row_num < 0:
            print('невозможно изменить значение - неверный номер строки матрицы')
            return
        if col_num > len(self.data[0]) or col_num < 0:
            print('невозможно изменить значение - неверный номер столбца матрицы')
            return
        if new_value < 1:
            print('Новое значение должно быть больше или равно 1!')
            return
        self.data[row_num][col_num] = new_value
        print(f'значение в ячейке [{row_num},{col_num}]  изменено на {new_value}')

    def showContents(self):
        '''Вывести все элементы матрицы'''
        for row_num in range(0, len(self.data)):
            print((self.data[row_num]))
            
matrix = Matrix(4, 7)
matrix.showSize()
matrix.showContents()
matrix.updateCell(0,0,666)
matrix.showContents()
del matrix