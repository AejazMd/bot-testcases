import unittest
from modules.equity import SimpleEquity
from modules.constants import EquityType

class TestSimpleEquity(unittest.TestCase):
    def setUp(self):
        self.common_equity = SimpleEquity("TEST", 10, 100, 0.0, EquityType.COMMON.value)
        self.preferred_equity = SimpleEquity("PREF", 0, 100, 0.05, EquityType.PREFERRED.value)

    def test_init(self):
        self.assertEqual(self.common_equity.ticker, "TEST")
        self.assertEqual(self.common_equity.lastDividend, 10)
        self.assertEqual(self.common_equity.parValue, 100)
        self.assertEqual(self.common_equity.fixedDividend, 0.0)
        self.assertEqual(self.common_equity.type, EquityType.COMMON.value)

    def test_get_dividend_yield_common(self):
        self.assertEqual(self.common_equity.getDividendYield(50), 0.20)

    def test_get_dividend_yield_preferred(self):
        self.assertEqual(self.preferred_equity.getDividendYield(100), 0.05)

    def test_get_price_to_earnings_ratio(self):
        self.assertEqual(self.common_equity.getPriceToEarningsRatio(50), 250)

    def test_is_valid(self):
        with self.assertRaises(ValueError):
            SimpleEquity("INVALID", 10, 100, 0.0, "invalid_type")

if __name__ == '__main__':
    unittest.main()