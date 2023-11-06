class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, salary_from, salary_to, name, employment, description, currency):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.name = name
        self.employment = employment
        self.description = description
        self.currency = currency

    def to_dict(self):
        """Преобразует объект класса Vacancy в словарь"""

        vacancy = {
            "name": self.name,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "employment": self.employment,
            "description": self.description,
            "currency": self.currency
        }
        return vacancy

    def __lt__(self, other):
        """Метод сравнения вакансий по зарплате"""

        if other.salary_from is None:
            return False
        if self.salary_from is None:
            return True
        return self.salary_from < other.salary_from

    def __str__(self):
        return f"{self.name}, {self.salary_from}, {self.employment}"
