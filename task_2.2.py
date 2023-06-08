# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

from calendar import month_name
import locale

#ставим русскую локаль, чтобы месяцы были на русском языке
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  
)

def quarter_of(month):
    '''Возвращает номер квартал по номеру месяца. В случае невалидного номера месяца возвращает -1'''
    if 1 <= month <= 3:
        return 1
    if 4 <= month <= 6:
        return 2
    if 7 <= month <= 9:
        return 3
    if 10 <= month <= 12:
        return 4
    return -1

month_number = int(input('Введите номер месяца как число от 1 до 12: '))
if 1 <= month_number <= 12:
    month_name = month_name[month_number]
    quarter_number = quarter_of(month_number)
    if quarter_number != -1:
        print(f'месяц {month_number} ({month_name}) является частью {quarter_number} квартала;')
else:
    print('Вы ввели неправильный номер месяца')        