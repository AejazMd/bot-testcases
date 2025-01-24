import unittest
from modules.constants import EquityType, TransactionType

class TestConstants(unittest.TestCase):
    def test_equity_type(self):
        self.assertEqual(EquityType.COMMON.value, "common")
        self.assertEqual(EquityType.PREFERRED.value, "preferred ")

    def test_transaction_type(self):
        self.assertEqual(TransactionType.BUY.value, "buy")
        self.assertEqual(TransactionType.SELL.value, "sell")

if __name__ == '__main__':
    unittest.main()