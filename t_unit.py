import unittest


class Calculator:
    def division(self, a, b):
        return a / b



class TestCalculator(unittest.TestCase):

    def test_div_error(self):
        self.calc = Calculator()
        self.assertRaises(ZeroDivisionError, self.calc.division, 10, 0)
    def test_isString(self):
        self.calc = Calculator()
        result = int(self.calc.division(22, 169)) 
        self.assertRaises(TypeError,result,True)
        
unittest.main(argv=[''], verbosity=2, exit=False)  