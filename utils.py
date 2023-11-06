from vacancy import Vacancy


def get_hh_vacancies(hh_vacancies):
    """Парсит и возвращает список вакансий с HH"""

    vacancies = []
    for vacancy in hh_vacancies:
        vacancies.append(
            Vacancy(
                name=vacancy.get("name"),
                description=vacancy.get("snippet")['requirement'],
                salary_to=vacancy.get("salary")['to'] if vacancy.get("salary").get('to') else None,
                salary_from=vacancy.get("salary")['from'] if vacancy.get("salary").get('from') else None,
                currency=vacancy.get("salary")['currency'],
                employment=vacancy.get("employer")['name']
            )
        )
    return vacancies

def get_sj_vacancies(sj_vacancies):
    """Парсит и возвращает список вакансий с Superjob"""

    vacancies = []
    for vacancy in sj_vacancies:
        Vacancy(
            name=vacancy.get("profession"),
            description=vacancy.get("snippet")["candidat"],
            salary_to=vacancy.get("payment_to") if vacancy.get("payment_to") else None,
            salary_from=vacancy.get("payment_from") if vacancy.get("payment_from") else None,
            currency=vacancy.get("salary")['currency'],
            employment=vacancy.get("employer")['name']
        )

    return vacancies
