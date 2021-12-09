# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

user_input_row = 'skjdhfkh skduhfksjdhf ksdjhf skdhfksjdh skdjhvkjsd slkfdjhvkjsdlckjsdkjhckjsdhkchskdjhvc'
user_input_row = input('Введите строку, разделяя слова пробелами: ')

for word in user_input_row.split(' '):
    if len(word) <= 10:
        print(word, f', количество символов в изначальном слове - {len(word)}')
    else:
        print(word[:10], f', количество символов в сокращённом варианте - {len(word[:10])}')
