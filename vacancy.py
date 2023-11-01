

class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, salary_from, salary_to, name, employment, description):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.name = name
        self.employment = employment
        self.description = description

    def get_vacancies(self):

        with open(f"{self.filename}.json", "w", encoding='utf-8') as f:
            data = json.load(f)


