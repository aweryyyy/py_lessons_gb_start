# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word: str) -> str:
    """
    Получаем строку, возвращаем строку с первым заглавным символом.
    """
    return word.capitalize()


print(int_func('dcksjdnc'))


def str_to_camel_case(string: str) -> str:
    """
    Получаем строку, возвращаем строку, где у каждого слова первая буква - заглавная.
    Используем метод перебора по списку, список формируем через разделение строки по split_symb.
    """
    split_symb = ' '
    work_list = string.split(split_symb)
    result = []
    for word in work_list:
        result.append(int_func(word))
    return ' '.join(result)


print(str_to_camel_case('dcksjdnc sdcjlskdjc sldcjlksdjc sdlcjlsdkjc sdlkcjsdkljc'))
