from .constants import EquityType


class SimpleEquity(object):
    '''
    class definition for an equity object to hold equity details and
    equity level calculations

    Attributes:
    -----------
    ticker: str
        unique identifier for a given equity
    lastDividend: float
        last dividend paid for a given equity
    parValue: float
        share value set by corporation'r charter
    fixedDividend: float
        fixed divided value for a given equity
    type: str, optional
        type of equity
    '''

    def __init__(self, ticker, lastDividend, parValue, fixedDividend, type='common'):
        '''
        Parameters:
        -----------
        ticker: str
        lastDividend: float
        parValue: float
        fixedDividend: float
        type: str, optional
        '''
        self.ticker = ticker.upper()
        self.lastDividend = lastDividend
        self.parValue = parValue
        self.fixedDividend = fixedDividend
        self.type = type
        self.isValid()
    

    def getDividendYield(self, price):
        '''
        Calculates dividend yield for given price

        Parameters:
        ----------
        price: float
            price of the given equity
        
        Returns:
        --------
        dividend yield
        '''
        if self.type == EquityType.COMMON.value:
            return round(self.lastDividend/price, 2)
        elif self.type == EquityType.PREFERRED.value:
            return round(self.fixedDividend*self.parValue/price, 2)
    

    def getPriceToEarningsRatio(self, price):
        '''
        Calculates Price to earning ratio

        Parameters:
        ----------
        price: float
            price of given equity
        '''
        return round(price/self.getDividendYield(price), 2)


    def isValid(self):
        '''
        Checks if the provided equity type is valid of not
        
        Raises:
        -------
        ValueError
            If known type is not given
        '''
        if self.type not in EquityType._value2member_map_.keys():
            raise ValueError('Invalid stock type given!')