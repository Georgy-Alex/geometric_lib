import math
import unittest

def area(r):
    ''' 
    Принимает радиус r
    Параметры:
        r (int): радиус круга
    Возвращаемое значение:
        возвращает площадь круга с радиусом r
    Например:
        def area(3):
        return math.pi * 3 * 3 Ответ: 28.2743338823
    ''' 
    return math.pi * r * r

def perimeter(r):
    '''  
    Принимает радиус r
    Параметры:
        r (int): радиус круга
    Возвращаемое значение:
        возвращает длину окружности круга с радиусом r
    Например:
        def perimeter(3):
        return 2 * math.pi * 3 Ответ: 18.8495559215
    '''
    return 2 * math.pi * r

# Встроенные тесты
class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        """Тест площади круга при радиусе 0"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        """Тест площади круга при положительном радиусе"""
        res = area(3)
        self.assertAlmostEqual(res, math.pi * 3 * 3, places=10)

    def test_area_large(self):
        """Тест площади круга для большого радиуса"""
        res = area(1000)
        self.assertAlmostEqual(res, math.pi * 1000 * 1000, places=10)

    def test_perimeter_zero(self):
        """Тест длины окружности при радиусе 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        """Тест длины окружности при положительном радиусе"""
        res = perimeter(3)
        self.assertAlmostEqual(res, 2 * math.pi * 3, places=10)

    def test_perimeter_large(self):
        """Тест длины окружности для большого радиуса"""
        res = perimeter(1000)
        self.assertAlmostEqual(res, 2 * math.pi * 1000, places=10)

