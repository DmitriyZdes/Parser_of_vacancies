from vacancy import Vacancy


def get_hh_vacancies(hh_vacancies):
    """Парсит и возвращает список вакансий с HH"""

    vacancies = []
    for vacancy in hh_vacancies:
        if vacancy.get("salary").get("to") is None or vacancy.get("salary").get("from") is None:
            continue
        else:
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
        if vacancy.get("payment_from") is None or vacancy.get("payment_to") is None:
            continue
        else:
            vacancies.append(
                Vacancy(
                    name=vacancy.get("profession"),
                    description=vacancy.get("candidat"),
                    salary_to=vacancy.get("payment_to") if vacancy.get("payment_to") else None,
                    salary_from=vacancy.get("payment_from") if vacancy.get("payment_from") else None,
                    currency=vacancy.get("currency"),
                    employment=vacancy.get("firm_name")
                )
            )

    return vacancies


def sort_vacancies(vacancies, count, order):
    """Сортирует вакансии по возрастанию-убыванию"""

    if count <= 0:
        print("Нет такой вакансии")

    if order.lower() == "да":
        return sorted(vacancies, reverse=True)[:count]
    elif order.lower() == "нет":
        return sorted(vacancies, reverse=False)[:count]
    else:
        return []
