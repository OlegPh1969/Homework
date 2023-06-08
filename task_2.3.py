# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    if 0 < number > 9:
        return "None"
    digit_values = ["Zero", "One", "Two", "Three", "Four", "Five",
                    "Six", "Seven", "Eight", "Nine" 
                    ]
    return digit_values[number]

for digit in range(11):
    value = switch_it_up(digit)
    print(f"switch_it_up({digit}) -> '{value}'")