from abc import ABC, abstractmethod
import requests

class BaseParser(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

class HhParser(BaseParser):
    """Класс для работы API HeadHunter"""

    def __init__(self):

        self.url = 'https://api.hh.ru/vacancies'
        self.params = {'only_with_salary': True, 'text': '', 'per_page': 100, 'page': 0}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['text'] = keyword
        while self.params['page'] != 20:
            response = requests.get(self.url, params=self.params)
            vacancies.extend(response.json()['items'])
            self.params['page'] += 1
        return vacancies



hh = HhParser()
print(hh.get_vacancies('python'))

