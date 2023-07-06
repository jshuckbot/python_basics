import csv
import sys
import logging
import argparse
from my_exceptions import ValidateError, ValidateFullNameError, ValidateEvaluationError
from validators import ValidatorFullName, ValidatorEvaluation

_EVALUATIONS = 'evaluations'
_TESTS = 'tests'
_TEXT_ERROR_GET_DATA = 'Вы ввели не корректные данные'
_TEXT_ERROR_SET_DATA = 'Можно добавлять только тесты и оценки по предметам!'

FORMAT = '{name} {levelname:<8} - {asctime}. №{lineno}: {msg}'
logging.basicConfig(format=FORMAT,
                    filename='logging.log',
                    encoding='utf-8',
                    style='{',
                    filemode='a',
                    level=logging.DEBUG, )
logger = logging.getLogger(__name__)


class Subject:
    """Предмет"""

    def __init__(self, name: str):
        self._name = name
        self._evaluations = []
        self._tests = []
        self._avg_tests = None
        self._avg_evaluations = None

    def __getitem__(self, item):
        match item:
            case 'tests':
                return self._tests
            case 'evaluations':
                return self._evaluations
            case 'avg_tests':
                return self._avg_tests
            case 'avg_evaluations':
                return self._avg_evaluations
            case _:
                raise KeyError(_TEXT_ERROR_GET_DATA)

    def __setitem__(self, key, value):
        match key:
            case 'tests':
                self._tests.append(value)
            case 'evaluations':
                self._evaluations.append(value)
            case _:
                raise KeyError(_TEXT_ERROR_SET_DATA)

    def __str__(self):
        return (f'{self._name}\n\t'
                f'Оценки: {self._evaluations};\n\t'
                f'Тесты: {self._tests};\n\t'
                f'Средний балл по тестам {self._count_avg_by_test():.2f}\n')

    def _count_avg_by_test(self) -> float:
        """Считает средний балл по тестам по каждому предмету"""
        return sum(self._tests) / len(self._tests)


class Student:
    """Студент"""
    f_name = ValidatorFullName()
    m_name = ValidatorFullName()
    l_name = ValidatorFullName()
    _cur_assessment = ValidatorEvaluation(2, 5)
    _cur_test = ValidatorEvaluation(0, 100)

    def __init__(self, f_name: str, m_name: str, l_name: str):
        try:
            self.f_name = f_name
            self.m_name = m_name
            self.l_name = l_name
        except ValidateFullNameError as ve:
            print(ve)
            sys.exit()
        self._cur_assessment = None
        self._cur_test = None
        self._total_evaluations = []
        self._subjects = self.__pull_subjects_from_csv()

    def __pull_subjects_from_csv(self) -> dict[str, Subject]:
        """Тянет предметы из csv файла"""
        file_csv = 'subjects.csv'

        with open(file_csv, 'r', encoding='utf-8', newline='') as csv_input:
            reader = csv.reader(csv_input, dialect='excel')

            return {row[-1].lower(): Subject(row[-1]) for row in reader}

    def set_the_subject_grade(self, subj: str, value: int) -> None:
        """Устанавливет оценку по предмету"""
        try:
            self._cur_assessment = value
        except ValidateEvaluationError as ve:
            logger.warning(ve)
            sys.exit()
        self._total_evaluations.append(value)
        self._subjects[subj.lower()][_EVALUATIONS] = self._cur_assessment

    def set_the_subject_test(self, subj: str, value: int) -> None:
        """Устанавливет оценку теста по предмету"""
        try:
            self._cur_test = value
        except ValidateEvaluationError as ve:
            logger.warning(ve)
            sys.exit()
        self._subjects[subj.lower()][_TESTS] = self._cur_test

    def get_grade_and_test_subjects(self):
        """Получить информацию по оценкам и тестам по предмету"""
        for key in self._subjects:
            print(self._subjects[key])

    def calc_avg_of_all_grades(self) -> str:
        """Считает cредний балл по оценкам всех предметов"""
        return (f'Средний балл по оценкам всех предметов '
                f'{sum(self._total_evaluations) / len(self._total_evaluations):.2f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='data puples')
    parser.add_argument('fullname', metavar='f_name m_name l_name', type=str, nargs=3,)
    fullname = parser.parse_args().fullname
    puple = Student(*fullname)
    # Оценки по предметам
    puple.set_the_subject_grade('Русский язык', 3)
    puple.set_the_subject_grade('Русский язык', 3)
    puple.set_the_subject_grade('Литература', 4)
    puple.set_the_subject_grade('Английский', 5)
    puple.set_the_subject_grade('Английский', 4)
    puple.set_the_subject_grade('Математика', 4)
    puple.set_the_subject_grade('Математика', 5)
    puple.set_the_subject_grade('Информатика', 5)
    puple.set_the_subject_grade('Информатика', 5)
    puple.set_the_subject_grade('Информатика', 5)
    puple.set_the_subject_grade('Физика', 5)
    puple.set_the_subject_grade('Физика', 5)
    puple.set_the_subject_grade('Физика', 4)
    # оценки по тестам
    puple.set_the_subject_test('Русский язык', 100)
    puple.set_the_subject_test('Русский язык', 60)
    puple.set_the_subject_test('Литература', 80)
    puple.set_the_subject_test('Английский', 77)
    puple.set_the_subject_test('Английский', 90)
    puple.set_the_subject_test('Математика', 100)
    puple.set_the_subject_test('Математика', 89)
    puple.set_the_subject_test('Информатика', 100)
    puple.set_the_subject_test('Информатика', 100)
    puple.set_the_subject_test('Информатика', 89)
    puple.set_the_subject_test('Физика', 70)
    puple.set_the_subject_test('Физика', 77)
    puple.set_the_subject_test('Физика', 60)

    puple.get_grade_and_test_subjects()
    print(puple.calc_avg_of_all_grades())
