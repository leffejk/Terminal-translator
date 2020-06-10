import requests
import terminal_translator_exceptions as ttexceptions

def main(TEXT:str, LANGUAGE:str, TRANSLATEKEY:str):
    URL = "https://translate.yandex.net/api/v1.5/tr.json/translate?" \
    + f"key={TRANSLATEKEY}" \
    + f"&text={TEXT}" \
    + f"&lang={LANGUAGE}"

    respone = requests.get(URL).json()['text'][0]
    
    if respone == TEXT:
        raise ttexceptions.TranslateError("Не удалось перевести текст")
    return "• " + respone
