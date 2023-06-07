# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

from datetime import datetime
import  calendar 
import locale

#ставим русскую локаль, чтобы месяцы были на русском языке
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  
)

# год нужен для calendar.monthrange
current_year = datetime.now().year

while 1 :
    month_number_s = input("Введите номер месяца или q для выхода: ")
    if month_number_s == "q" :
        break;
    month_number_int = int(month_number_s)
    if 1 <= month_number_int <= 12 :
        days_in_month = calendar.monthrange(current_year, month_number_int)[1]
        month_s = calendar.month_name[month_number_int]
        print(f'Вы ввели {month_s}. {days_in_month} дней')
    else :
        print('Такого месяца нет!')