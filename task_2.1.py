# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

#массивы для сортировки
data = [ [ 4,6,2,1,9,63,-134,566],
         [-52, 56, 30, 29, -54, 0, -110], 
         [42, 54, 65, 87, 0],
         [5]  
] 

def gnomeSort( arrOld ):
    '''Гномья сортировка. Возвращает сортированную КОПИЮ исходного массива'''
    n = len(arrOld)
    # для случая с одним элементом просто возвращаем исходный массив
    if n == 1:
        return arrOld 
    
    arr = arrOld.copy()
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
    return arr

def minimum(arr):
    sorted = gnomeSort(arr)
    return sorted[0]

def maximum(arr):
    sorted = gnomeSort(arr)
    return sorted[len(sorted) - 1]

#цикл по всем массивам для сортировки
for cur_arr in data:
    max, min = maximum(cur_arr), minimum(cur_arr)
    print(f'{cur_arr} -> max = {max}, min = {min} ')
