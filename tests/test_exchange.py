import unittest
from modules.exchange import SimpleStockExchange
from modules.equity import SimpleEquity
from modules.constants import EquityType, TransactionType

class TestSimpleStockExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = SimpleStockExchange()

    def test_init(self):
        self.assertEqual(self.exchange.name, "Simple Stock Exchange")
        self.assertEqual(len(self.exchange.listedEquity), 5)

    def test_add_stock_to_index(self):
        new_equity = SimpleEquity("NEW", 5, 50, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(new_equity)
        self.assertTrue(self.exchange.isStockListed("NEW"))

    def test_buy_stock(self):
        initial_transactions = len(self.exchange.equityTransactions["TEA"])
        self.exchange.buyStock("TEA", 100, 1000)
        self.assertEqual(len(self.exchange.equityTransactions["TEA"]), initial_transactions + 1)

    def test_sell_stock(self):
        initial_transactions = len(self.exchange.equityTransactions["TEA"])
        self.exchange.sellStock("TEA", 50, 1100)
        self.assertEqual(len(self.exchange.equityTransactions["TEA"]), initial_transactions + 1)

    def test_get_stock(self):
        stock = self.exchange.getStock("TEA")
        self.assertIsInstance(stock, SimpleEquity)
        self.assertEqual(stock.ticker, "TEA")

    def test_get_stock_details(self):
        details = self.exchange.getStockDetails()
        self.assertEqual(len(details), 5)
        self.assertIn("Ticker", details[0])

    def test_get_stock_transactions(self):
        transactions = self.exchange.getStockTransactions("TEA")
        self.assertGreater(len(transactions), 0)
        self.assertIn("Ticker", transactions[0])

    def test_get_volume_weighted_stock_price(self):
        price = self.exchange.getVolumeWeightedStockPrice("TEA")
        self.assertIsInstance(price, float)

    def test_get_gbce(self):
        gbce = self.exchange.getGBCE()
        self.assertIsInstance(gbce, float)

    def test_remove_stock_from_index(self):
        new_equity = SimpleEquity("REMOVE", 5, 50, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(new_equity)
        self.exchange.removeStockFromIndex(new_equity)
        self.assertFalse(self.exchange.isStockListed("REMOVE"))

if __name__ == '__main__':
    unittest.main()