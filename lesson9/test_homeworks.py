from lesson9.homeworks import sum_of_elements
from lesson9.homeworks import data
from lesson9.homeworks import compare_grades
import unittest


class MyTest(unittest.TestCase):
    def test_int_value(self):
        result = sum_of_elements(['1,2,3', '4,4,5'])
        self.assertEqual([6, 13], result)

    def test_value_error(self):
        result = sum_of_elements(['as', 'ad'])
        self.assertEqual('Error', result)

    def test_float_value(self):
        result = sum_of_elements(['1.5, 1.8', '5.1, 7.2'])
        self.assertEqual([3.3, 12.3], result)

    def test_data_int_value(self):
        result = data(2, 3, 2002)
        self.assertEqual('02.03.2002', result)

    def test_data_float_value(self):
        result = data(2.3, 5.5, 2002.2)
        self.assertEqual('Error', result)

    def test_data_str_value(self):
        result = data('23', '07', '2002')
        self.assertEqual('Error', result)

    def test_data_separator(self):
        result = data(8, 9, 2002, sep='/')
        self.assertEqual('08/09/2002', result)

    def test_grades_int(self):
        result = compare_grades({'Анна Коваленко': 90, 'Олег Петров': 85}, {'Анна Коваленко': 92, 'Олег Петров': 87})
        self.assertEqual({'Анна Коваленко': -2, 'Олег Петров': -2}, result)

    def test_grades_float(self):
        result = compare_grades({'Анна Коваленко': 90.2, 'Олег Петров': 85.5}, {'Анна Коваленко': 92, 'Олег Петров': 87})
        self.assertEqual('Error', result)

    def test_grades_str(self):
        result = compare_grades({'Анна Коваленко': '92', 'Олег Петров': '85'}, {'Анна Коваленко': 92, 'Олег Петров': 87})
        self.assertEqual('Error', result)

    def test_grades_none(self):
        result = compare_grades({}, {'Анна Коваленко': 92, 'Олег Петров': 87})
        print('AR:', result)
        self.assertEqual({'Анна Коваленко': -92, 'Олег Петров': -87}, result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
