import unittest

def area(a, b):
    ''' 
    Принимает длину и ширину прямоугольника
    Параметры:
        a (int): длина прямоугольника
        b (int): ширина прямоугольника
    Возвращаемое значение:
        возвращает площадь прямоугольника
    Например:
        def area(4, 5):
        return 4 * 5 Ответ: 20
    '''
    return a * b

def perimeter(a, b):
    '''  
    Принимает длину и ширину прямоугольника
    Параметры:
        a (int): длина прямоугольника
        b (int): ширина прямоугольника
    Возвращаемое значение:
        возвращает периметр прямоугольника (int)
    Например:
        def perimeter(4, 5):
        return 2 * (4 + 5) Ответ: 18
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    # Тесты для функции area
    def test_area_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0, "Площадь должна быть равна 0, если одна из сторон равна 0")
    
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100, "Площадь квадрата со стороной 10 должна быть равна 100")
    
    def test_area_general(self):
        res = area(4, 5)
        self.assertEqual(res, 20, "Площадь прямоугольника со сторонами 4 и 5 должна быть равна 20")
    
    # Тесты для функции perimeter
    def test_perimeter_zero_side(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20, "Периметр должен быть равен 2 * длина, если ширина равна 0")
    
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40, "Периметр квадрата со стороной 10 должен быть равен 40")
    
    def test_perimeter_general(self):
        res = perimeter(4, 5)
        self.assertEqual(res, 18, "Периметр прямоугольника со сторонами 4 и 5 должен быть равен 18")

# Проверяем запуск тестов
# if __name__ == "__main__":
#     unittest.main()