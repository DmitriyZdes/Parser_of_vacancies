from parser1 import HH, SJ
from utils import get_hh_vacancies, get_sj_vacancies
from json_saver import JSONSaver

def main():

    print("Приветствуем, представляем парсер вакансий")
    keyword = input("Введите слово для поиска ")
    hh = HH()
    sj = SJ()
    hh_vacancies = hh.get_vacancies(keyword)
    sj_vacancies = sj.get_vacancies(keyword)
    hh_vacancies = get_hh_vacancies(hh_vacancies)
    sj_vacancies = get_sj_vacancies(sj_vacancies)
    vacancies = hh_vacancies + sj_vacancies
    vacancies_json = JSONSaver('vacancies')
    vacancies_json.write_json(vacancies)
    print(vacancies_json.sort(reverse=True)[:2])

main()