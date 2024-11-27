import unittest

def area_square_on_the_coordinate_system(a):
    """Функция для вычисления площади квадрата по длине стороны."""
    return a * a

class SquareTestCase(unittest.TestCase):
    """Класс для тестирования функции area_square_on_the_coordinate_system."""

    def test_area_of_square_with_positive_side(self):
        result = area_square_on_the_coordinate_system(10)
        self.assertEqual(result, 100)

    def test_area_of_square_with_zero_side(self):
        result = area_square_on_the_coordinate_system(0)
        self.assertEqual(result, 0)

    def test_area_of_square_with_negative_side(self):
        result = area_square_on_the_coordinate_system(-10)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    # Запуск тестов, если файл запускается как основной модуль
    unittest.main()
