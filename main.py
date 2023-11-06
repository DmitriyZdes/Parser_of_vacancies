from parser1 import HH, SJ
from utils import get_hh_vacancies, get_sj_vacancies, sort_vacancies
from json_saver import JSONSaver


def main():
    """Основная функция программы для поиска вакансий"""

    print("Приветствуем, представляем парсер вакансий")
    keyword = input("Введите слово для поиска ")
    if keyword.lower() == "выход":
        print("Завершение программы")
    hh = HH()
    sj = SJ()
    hh_vacancies = hh.get_vacancies(keyword)
    sj_vacancies = sj.get_vacancies(keyword)
    hh_vacancies = get_hh_vacancies(hh_vacancies)
    sj_vacancies = get_sj_vacancies(sj_vacancies)
    vacancies = hh_vacancies + sj_vacancies
    vacancies_json = JSONSaver('vacancies')
    vacancies_json.write_json(vacancies)
    count = input("Введите количество желаемых вакансий для вывода ")
    order = input("Отсортировать по убыванию? Да/Нет ")
    vacancies = sort_vacancies(vacancies, int(count), order)
    for vacancy in vacancies:
        print(vacancy)


main()
