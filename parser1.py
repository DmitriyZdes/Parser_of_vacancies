from abc import ABC, abstractmethod
import requests
import os


class BaseParser(ABC):
    """Абстрактный класс-парсер"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HH(BaseParser):
    """Класс для парсинга вакансий с HH.ru"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'only_with_salary': True, 'text': '', 'per_page': 100, 'page': 0}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['text'] = keyword
        while self.params['page'] != 20:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            vacancies.extend(response.json()['items'])
            self.params['page'] += 1
        return vacancies


class SJ(BaseParser):
    """Класс для парсинга вакансий с Superjob"""

    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.headers = {'X-Api-App-Id': os.getenv('SJ_KEY')}
        self.params = {'keyword': '', 'count': 100, 'page': 0}

    def get_vacancies(self, keyword):
        vacancies = []
        self.params['keyword'] = keyword
        while self.params.get('page') != 5:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies.extend(response.json()['objects'])
            self.params['page'] += 1
        return vacancies
