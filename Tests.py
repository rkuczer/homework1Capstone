import unittest

from main import calculate_total


class TestCalculateTotal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = [
            {'name': 'Sneakers', 'type': 'Clothing', 'price': 50.00},
            {'name': 'jeans', 'type': 'Clothing', 'price': 75.00},
            {'name': 'Fur coat', 'type': 'Clothing', 'price': 200.00},
            {'name': 'log', 'type': 'everything else', 'price': 100.00},
            {'name': 'apple', 'type': 'Wic Eligible food', 'price': 100.00}
        ]
    def test_NJ(self):
        state = 'NJ'
        result = calculate_total(state, self.records)
        self.assertEqual(result, 544.80)

    def test_PA(self):
        state = 'PA'
        result = calculate_total(state, self.records)
        self.assertEqual(result, 531.00)

    def test_DE(self):
        state = 'DE'
        result = calculate_total(state, self.records)
        self.assertEqual(result, 525.00)


if __name__ == '__main__':
    unittest.main()
