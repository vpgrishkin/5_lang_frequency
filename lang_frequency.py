import re
import sys
import os
from collections import Counter


DEFAULT_FILE_NAME = 'default.txt'
DEFAULT_NUMBER_COMMON_WORDS = 10


def load_data(file_path):
    with open(file_path, 'rt') as file:
        file_text = file.read()
        return file_text.lower()


def get_most_frequent_words(text):
    words_from_text = re.findall('\w+', text)
    most_frequent_words = []
    most_frequent_words = Counter(words_from_text).most_common(DEFAULT_NUMBER_COMMON_WORDS)
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска! Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        work_file = sys.argv[1]
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)

    text = load_data(work_file)
    top10_frequent_words = get_most_frequent_words(text)
    print('10 самых частотных слов:')
    for word in top10_frequent_words:
        print('Слово {} встречается {} раз.'.format(word[0], word[1]))