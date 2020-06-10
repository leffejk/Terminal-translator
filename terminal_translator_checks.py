import terminal_translator_exceptions as ttexceptions

englishAlphabet = [chr(i) for i in range(65,90+1)] + [chr(i) for i in range(97, 122+1)]
russianAlphabet = [chr(i) for i in range(1040,1103+1)] + ["Ё", "ё"]

def language_detector(text: str):
    for letter in text:
        if letter in englishAlphabet:
            return "en-ru"
        elif letter in russianAlphabet:
            return "ru-en"
    raise ttexceptions.LanguageDecectorError("Не удалось определить язык")


def text_check(text: str):
    if len(text) == 0:
        raise ttexceptions.TextLengthError("Строка для перевода не может быть пустой")
    return text
