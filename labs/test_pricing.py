"""test_pricing.py"""
import unittest

from pricing import calculate

class TestPricing(unittest.TestCase):
    """TestPricing class"""
    def test_calculate(self):
        """test_calculate method"""
        items = (
            {'case': 'No tax, no discount', 'price': 10, 'tax': 0, 'discount': 0, 'net_price': 10},
            {'case': 'Has tax, no discount', 'price': 10, 'tax': 0.1, 'discount': 0,
            'net_price': 11},
            {'case': 'No tax, has discount', 'price': 10, 'tax': 0, 'discount': 1,
            'net_price': 9},
            {'case': 'Has tax, has discount', 'price': 10, 'tax': 0.1, 'discount': 1,
            'net_price': 9.9},
        )
        for item in items:
            with self.subTest(item['case']):
                net_price = calculate(item['price'], item['tax'], item['discount'])
                self.assertEqual(net_price,item['net_price'])
