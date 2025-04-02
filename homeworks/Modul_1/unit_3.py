"""создать функцию посчета слов из списка в котором встерчается конкретная буква"""

def count_words(words, leter):
    count = 0
    for i in words:
        for ltr in i:
            if ltr == leter:
                count += 1
                break
    return count


text = ['python', 'c++', 'c', 'scala', 'java']

chart = input('Введите букву в слове - ')

print(f'количество слов в которых есть буква {chart} - {count_words(text, chart)} штук')
