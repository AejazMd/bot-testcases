import unittest
from modules.exchange import SimpleStockExchange
from modules.equity import SimpleEquity
from modules.constants import EquityType

class TestSimpleStockExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = SimpleStockExchange()

    def test_add_stock_to_index(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(equity)
        self.assertTrue(self.exchange.isStockListed('AAPL'))

    def test_add_duplicate_stock(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(equity)
        with self.assertRaises(ValueError):
            self.exchange.addStockToIndex(equity)

    def test_buy_stock(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(equity)
        self.exchange.buyStock('AAPL', 10, 150)
        transactions = self.exchange.getStockTransactions('AAPL')
        self.assertEqual(len(transactions), 1)

    def test_buy_non_existing_stock(self):
        with self.assertRaises(ValueError):
            self.exchange.buyStock('NONEXIST', 10, 150)

    def test_sell_stock(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(equity)
        self.exchange.buyStock('AAPL', 10, 150)
        self.exchange.sellStock('AAPL', 5, 155)
        transactions = self.exchange.getStockTransactions('AAPL')
        self.assertEqual(len(transactions), 2)

    def test_sell_non_existing_stock(self):
        with self.assertRaises(ValueError):
            self.exchange.sellStock('NONEXIST', 5, 150)

    def test_get_stock(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.exchange.addStockToIndex(equity)
        fetched_equity = self.exchange.getStock('AAPL')
        self.assertEqual(fetched_equity.ticker, 'AAPL')

    def test_get_stock_not_found(self):
        with self.assertRaises(ValueError):
            self.exchange.getStock('NONEXIST')


if __name__ == '__main__':
    unittest.main()