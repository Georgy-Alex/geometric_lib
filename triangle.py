import unittest

def area(a):
    ''' 
    Принимает длину стороны квадрата
    Параметры:
        a (int): длина стороны квадрата
    Возвращаемое значение:
        возвращает площадь квадрата
    Например:
        def area(4):
        return 4 * 4 Ответ: 16
    '''
    return a * a

def perimeter(a):
    ''' 
    Принимает длину стороны квадрата
    Параметры:
        a (int): длина стороны квадрата
    Возвращаемое значение:
        возвращает периметр квадрата
    Например:
        def perimeter(4):
        return 4 * 4 Ответ: 16
    '''
    return 4 * a


# Встроенные тесты
class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        """Тест площади квадрата при длине стороны 0"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        """Тест площади квадрата при положительной длине стороны"""
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_large(self):
        """Тест площади квадрата для большой длины стороны"""
        res = area(1000)
        self.assertEqual(res, 1000000)

    def test_perimeter_zero(self):
        """Тест периметра квадрата при длине стороны 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        """Тест периметра квадрата при положительной длине стороны"""
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_large(self):
        """Тест периметра квадрата для большой длины стороны"""
        res = perimeter(1000)
        self.assertEqual(res, 4000)

