import unittest

from main import calculate_total


# User input is required for the tests then they will run. Just is due to my structuring of functions in main.py


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

    def test_no_records(self):
        state = 'NJ'
        records = []
        result = calculate_total(state, records)
        self.assertEqual(result, 0)

    def test_negative_priced_item(self):
        state = 'PA'
        records = [{'name': 'jeans', 'type': 'Clothing', 'price': -75.00}]
        self.assertEqual(calculate_total(state, records), 0.0)

    def test_calculate_total_edge_cases(self):
        self.assertEqual((calculate_total('NJ', [])), 0.0)

    def test_addition(self):
        # Test with all tax-exempt items
        records = [
            {'name': 'apple', 'type': 'Wic Eligible food', 'price': 1.00},
            {'name': 'banana', 'type': 'Wic Eligible food', 'price': 2.00},
            {'name': 'shirt', 'type': 'Clothing', 'price': 10.00},
            {'name': 'shoes', 'type': 'Clothing', 'price': 20.00},
        ]
        self.assertEqual((calculate_total('NJ', records)), (sum(item['price'] for item in records)))


if __name__ == '__main__':
    unittest.main()
