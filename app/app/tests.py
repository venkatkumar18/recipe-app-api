
from django.test import SimpleTestCase
from . import calc

class CalculationTestCase(SimpleTestCase):

    def test_add_two_numbers(self):
        result = calc.add_two_number(18, 38)
        self.assertEqual(result, 56)

    def test_subtract_two_number(self):
        result = calc.subtract(90,80)
        self.assertEqual(result, 10)