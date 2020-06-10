import requests

def format_list_helper(object_: list, object_name: str):
    return_string = object_name + ": "
    for section in object_:
        # object_name: word (
        return_string += section["text"] + "("
        # object_name: word (часть_речи;
        try: return_string += section["pos"] + ";"
        except: pass
        # object_name: word (часть_речи;род;
        try: return_string += section["gen"] + ";"
        except: pass
        # object_name: word (часть_речи;род;число;
        try: return_string += section["num"] + ";"
        except: pass

        # object_name: word (часть_речи;род;число;);
        return_string += "); "

        if "tr" in section:
            return_string += "\n" + format_list_helper(section["tr"], "Переводы")
    return return_string + "\n"



def format_list(translation:list):
    return_string = ""
    if type(translation) == list:
        for section in translation:
            # Форматирование раздела "Перевод"
            return_string += "Перевод: " + section["text"] + " ("
            try: return_string += section["pos"] + ";"
            except: pass
            try: return_string += section["gen"] + ";"
            except: pass 
            try: return_string += section["num"] + ";"
            except: pass
            return_string += ");\n"

            # Добавление пунктов: синонимы, значения, примеры
            try: return_string += format_list_helper(section["syn", "Синонимы"])
            except: pass
            try: return_string += format_list_helper(section["mean", "значения"])
            except: pass
            try: return_string += format_list_helper(section["ex", "Примеры"])
            except: pass
        return return_string



def format_response(response: list):
    ''' Форматирование ответа в читаемый вид '''
    formatted_list = []

    for translation_variant in response:
        section = list(translation_variant.values())
        formatted_list.append(
            "• " + section[0] + " (" + ", ".join(section[1:-1]) + ");\n"\
            + format_list(section[-1])
            )
    return formatted_list


def main(TEXT:str, LANGUAGE:str, DICTKEY:str):
    URL = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?" \
    + f"key={DICTKEY}" \
    + f"&lang={LANGUAGE}" \
    + f"&text={TEXT}" \
    + "&ui=ru"
    
    response = requests.get(URL).json()["def"]
    temp_string = "\n".join([line for line in  format_response(response)])

    # Финальное форматирование
    temp_string = temp_string.replace(";)", ")").replace("()", "")
    return_list = [""]
    for string in temp_string.split("\n"):
        if string.replace(" ","").replace(";","").isalpha():
            return_list.append("Пример: " + string)
        else:
            return_list.append(string)
            
    return "\n".join(return_list)

