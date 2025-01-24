import unittest
from modules.constants import EquityType, TransactionType

class TestConstants(unittest.TestCase):

    def test_equity_type_values(self):
        self.assertEqual(EquityType.COMMON.value, "common")
        self.assertEqual(EquityType.PREFERRED.value, "preferred ")

    def test_transaction_type_values(self):
        self.assertEqual(TransactionType.BUY.value, "buy")
        self.assertEqual(TransactionType.SELL.value, "sell")

    def test_equity_type_iteration(self):
        equity_types = [equity_type.value for equity_type in EquityType]
        self.assertEqual(equity_types, ["common", "preferred "])

    def test_transaction_type_iteration(self):
        transaction_types = [transaction_type.value for transaction_type in TransactionType]
        self.assertEqual(transaction_types, ["buy", "sell"])

