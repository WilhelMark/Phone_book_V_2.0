def from_file(file):
    """Читает информацию из текстового файла и выводит ее в консоль"""
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary