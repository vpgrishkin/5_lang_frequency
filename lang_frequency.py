import re
import sys
import os
from collections import Counter


DEFAULT_NUMBER_COMMON_WORDS = 10


def load_data(file_path):
    with open(file_path, 'rt') as file:
        return file.read()


def get_most_frequent_words(text):
    words_from_text = re.findall('\w+', text.lower())
    most_frequent_words = Counter(words_from_text).most_common(DEFAULT_NUMBER_COMMON_WORDS)
    return most_frequent_words


def imput_file_name_or_exit():
    if len(sys.argv) == 1:
        print('Нет параметров для запуска')
        work_file = input('Введите имя файла:')
    else:
        work_file = sys.argv[1]
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)
    
    return work_file


if __name__ == '__main__':
    work_file_name = imput_file_name_or_exit()
    text = load_data(work_file_name)
    top10_frequent_words = get_most_frequent_words(text)
    print('10 самых частотных слов:')
    for word in top10_frequent_words:
        print('Слово {} встречается {} раз.'.format(word[0], word[1]))