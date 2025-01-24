import unittest
from modules.constants import EquityType, TransactionType

class TestConstants(unittest.TestCase):

    def test_equity_type_values(self):
        self.assertEqual(EquityType.COMMON.value, "common")
        self.assertEqual(EquityType.PREFERRED.value, "preferred")

    def test_transaction_type_values(self):
        self.assertEqual(TransactionType.BUY.value, "buy")
        self.assertEqual(TransactionType.SELL.value, "sell")

    def test_equity_type_membership(self):
        self.assertIn(EquityType.COMMON, EquityType)
        self.assertIn(EquityType.PREFERRED, EquityType)
        self.assertNotIn("common", EquityType)  # Test for incorrect membership check
        with self.assertRaises(ValueError):
            EquityType("invalid")

    def test_transaction_type_membership(self):
        self.assertIn(TransactionType.BUY, TransactionType)
        self.assertIn(TransactionType.SELL, TransactionType)
        self.assertNotIn("buy", TransactionType) # Test for incorrect membership check
        with self.assertRaises(ValueError):
            TransactionType("invalid")