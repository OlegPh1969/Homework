# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    if len(s) == 0:
        return ""
    return s.replace('!', '') 

def run_remove_exclamation_marks_and_print_result(str) :
    str_removed = remove_exclamation_marks(str)
    print(f'remove_exclamation_marks("{str}") -> "{str_removed}"')

run_remove_exclamation_marks_and_print_result("Hi! Hello!")
run_remove_exclamation_marks_and_print_result("")
run_remove_exclamation_marks_and_print_result("Oh, no!!!")

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[-1] == '!':
        return s[0:-1]
    else:
        return s

def run_remove_last_em_and_print_result(str) :
    str_removed = remove_last_em(str)
    print(f'remove_last_em("{str}") == "{str_removed}"')

run_remove_last_em_and_print_result("Hi!")
run_remove_last_em_and_print_result("Hi!!!")
run_remove_last_em_and_print_result("!Hi")

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    removed_s = ""
    for word in s.split():
        if word.count('!') != 1:
            removed_s += word + ' '
    if  len(removed_s) > 0:
        removed_s = removed_s[:-1]       
    return removed_s
            
def run_remove_word_with_one_em_and_print_result(str):
    str_removed = remove_word_with_one_em(str)
    print(f'remove_word_with_one_em("{str}") === "{str_removed}"')
print('-------------------------------------------')
run_remove_word_with_one_em_and_print_result("Hi!")
run_remove_word_with_one_em_and_print_result("Hi! Hi!")
run_remove_word_with_one_em_and_print_result("Hi! Hi! Hi!")
run_remove_word_with_one_em_and_print_result("Hi Hi! Hi!")
run_remove_word_with_one_em_and_print_result("Hi! !Hi Hi!")
run_remove_word_with_one_em_and_print_result("Hi! Hi!! Hi!")
run_remove_word_with_one_em_and_print_result("Hi! !Hi! Hi!")