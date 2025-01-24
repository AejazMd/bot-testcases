import unittest
from modules.constants import EquityType, TransactionType

class TestConstants(unittest.TestCase):
    def test_equity_types(self):
        self.assertEqual(EquityType.COMMON.value, 'common')
        self.assertEqual(EquityType.PREFERRED.value, 'preferred')
        self.assertIn('common', EquityType._value2member_map_)
        self.assertIn('preferred', EquityType._value2member_map_)

    def test_transaction_types(self):
        self.assertEqual(TransactionType.BUY.value, 'buy')
        self.assertEqual(TransactionType.SELL.value, 'sell')
        self.assertIn('buy', TransactionType._value2member_map_)
        self.assertIn('sell', TransactionType._value2member_map_)


if __name__ == '__main__':
    unittest.main()}