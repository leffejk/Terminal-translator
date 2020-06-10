# -*- coding: utf-8 -*-

import terminal_translator_checks as ttchecks
import terminal_translator_exceptions as ttexceptions

import terminal_translator_gotranslate as ttgotranslate
import terminal_translator_godict as ttgodict
from sys import argv
import configparser


def main():
    # Читаем конфигурационный файл config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Определяем строку и язык для перевода, а так-же API KEYS
    try:
        TEXT = ttchecks.text_check(argv[1])
    except IndexError:
        raise ttexceptions.ArgumentError(
            "Нужно указать текст для перевода в качестве первого аргумента")
    LANGUAGE = ttchecks.language_detector(TEXT)
    try:
        DICTKEY = config['main']['dict_key']
        TRANSLATEKEY = config['main']['translate_key']
    except:
        raise ttexceptions.ConfigError("Ошибка чтения ключей из config.ini")

    print()
    # Если в качестве аргумента передается одно слово, то используется API Словаря
    # Иначе, используется API Переводчика
    if len(TEXT.split()) == 1:
        print(ttgodict.main(TEXT, LANGUAGE, DICTKEY))
    else:
        print(ttgotranslate.main(TEXT, LANGUAGE, TRANSLATEKEY))



if __name__ == '__main__':
    main()
