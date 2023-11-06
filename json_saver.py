import json


class JSONSaver:
    """Класс для загрузки вакансий в файл json-формат"""

    def __init__(self, filename):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def write_json(self, vacancies):

        with open(f"{self.filename}.json", "w", encoding='utf-8') as f:
            json.dump([vacancy.to_dict() for vacancy in vacancies], f)
