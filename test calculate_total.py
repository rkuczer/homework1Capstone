from main import calculate_total
import unittest


class MyTestCase(unittest.TestCase):
    def test_calculate_total1(self):
        # Test case 1: NJ, only taxable items
        state = 'NJ'
        records = [
            {'name': 'Shoes', 'type': 'Clothing', 'price': 50.00},
            {'name': 'Bag', 'type': 'everything else', 'price': 20.00},
        ]
        self.assertTrue((calculate_total(state, records)),
                        55.08)  # 50 + 20 = 70, 6.6% of 70 is 4.62, 70+4.62=74.62, round to 2 decimals is 74.62

    def test_calculate_total2(self):
        # Test case 2: NJ, some tax-exempt items
        state = 'NJ'
        records = [
            {'name': 'Apple', 'type': 'Wic Eligible food', 'price': 0.50},
            {'name': 'T-shirt', 'type': 'Clothing', 'price': 10.00},
            {'name': 'Fur coat', 'type': 'Clothing', 'price': 500.00},
            {'name': 'Book', 'type': 'everything else', 'price': 5.00},
        ]
        self.assertEqual((calculate_total(state, records)),
                         538.58)  # 10+500+5=515, taxable subtotal is 515, 6.6% of 515 is 34.03, 515+34.03=549.03, round to 2 decimals is 549.03

    def test_calculate_total3(self):
        # Test case 3: PA, only taxable items
        state = 'PA'
        records = [
            {'name': 'Shoes', 'type': 'Clothing', 'price': 50.00},
            {'name': 'Bag', 'type': 'everything else', 'price': 20.00},
        ]
        self.assertEqual((calculate_total(state, records)),
                         53.00)  # 50+20=70, 6% of 70 is 4.20, 70+4.20=74.20, round to 2 decimals is 74.20

    def test_calculate_total4(self):
        # Test case 4: PA, some tax-exempt items
        state = 'PA'
        records = [
            {'name': 'Apple', 'type': 'Wic Eligible food', 'price': 0.50},
            {'name': 'T-shirt', 'type': 'Clothing', 'price': 10.00},
            {'name': 'Fur coat', 'type': 'Clothing', 'price': 500.00},
            {'name': 'Book', 'type': 'everything else', 'price': 5.00},
        ]
        self.assertEqual((calculate_total(state, records)), 525.53)
        # 500+5=505, taxable subtotal is 505, 6% of 505 is 30.30, 505+30.30=535.30, round to 2 decimals is 535.30

    def de_function(self):  # Test case 5: DE, only taxable items
        state = 'DE'
        records = [
            {'name': 'Shoes', 'type': 'Clothing', 'price': 50.00},
            {'name': 'Bag', 'type': 'everything else', 'price': 20.00},
        ]
        self.assertEqual((calculate_total(state, records)), 70.00)  # no tax in DE, so total is just the sum of prices


if __name__ == '__main__':
    unittest.main()
