import unittest
from modules.equity import SimpleEquity
from modules.constants import EquityType

class TestSimpleEquity(unittest.TestCase):
    def test_initialization(self):
        equity = SimpleEquity('AAPL', 0.5, 100, 0.02)
        self.assertEqual(equity.ticker, 'AAPL')
        self.assertEqual(equity.lastDividend, 0.5)
        self.assertEqual(equity.parValue, 100)
        self.assertEqual(equity.fixedDividend, 0.02)
        self.assertEqual(equity.type, 'common')

    def test_invalid_equity_type(self):
        with self.assertRaises(ValueError):
            SimpleEquity('AAPL', 0.5, 100, 0.02, type='invalid')
    
    def test_get_dividend_yield_common(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0, EquityType.COMMON.value)
        self.assertEqual(equity.getDividendYield(100), 0.01)
    
    def test_get_dividend_yield_preferred(self):
        equity = SimpleEquity('AAPL', 0.0, 100, 0.02, EquityType.PREFERRED.value)
        self.assertEqual(equity.getDividendYield(100), 0.02)
    
    def test_get_dividend_yield_zero_price(self):
        equity = SimpleEquity('AAPL', 1.0, 100, 0.0)
        with self.assertRaises(ZeroDivisionError):
            equity.getDividendYield(0)
    
    def test_get_pe_ratio(self):
        equity = SimpleEquity('AAPL', 2.0, 100, 0.0)
        self.assertEqual(equity.getPriceToEarningsRatio(100), 50.0)
    
    def test_is_valid(self):
        equity = SimpleEquity('AAPL', 2.0, 100, 0.0)
        self.assertIsNone(equity.isValid())

    def test_invalid_equity_validation(self):
        equity = SimpleEquity('AAPL', 2.0, 100, 0.0, type='invalid')
        with self.assertRaises(ValueError):
            equity.isValid()


if __name__ == '__main__':
    unittest.main()