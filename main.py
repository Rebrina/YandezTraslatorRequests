import requests


def translate_it(text_for_translate, file_translated, lang, lang_to_translate):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181206T210101Z.0c17b40d4f148017.89e0ac198607ce8699dad017ab58961bd2e4fe3f'

    lang = lang + '-' + lang_to_translate

    params = {
        'key': key,
        'lang': lang,
        'text': text_for_translate
    }
    # response = requests.get(url, params=params).json()
    response = requests.post(url, params=params, timeout=30).json()
    a = response.get('text', [])
    with open(file_translated, 'w') as f:
        f.write(a[0])
    print(a)
    # return ' '.join(response.get('text', []))


# взять файл из текущей директории (путь к файлам) и передать в функцию

if __name__ == "__main__":
    file_name = input('Введите путь к файлу текста ')
    file_translated = input('Введите название файлаЮ куда будет записан перевод')
    lang = input('Введите язык, с которого нужно перевести (например, de,es,fr ')
    lang_to_translate = input('Введите язык, на который нужно перевести (например, ru) ')

    text_for_translate = ''

    with open(file_name, encoding="utf-8") as f:
        for line in f:
            if line > '':
                text_for_translate = text_for_translate + line.strip() + ''

    translate_it(text_for_translate, file_translated, lang, lang_to_translate)





