from json import dump, load


class JSONDriver:
    def __init__(self, path: str):
        self._path = path

    def load_data(self):
        with open(self._path, 'r', encoding='utf-8') as data:
            result = load(data)
        return result

    def save_data(self, data: dict):
        with open (self._path, 'w', encoding='utf-8') as file:
            dump(data, file)
