import numpy as np

from time import time
from .equity import SimpleEquity
from collections import defaultdict
from datetime import datetime, timedelta
from .constants import EquityType, TransactionType

class SimpleStockExchange(object):
    '''
    class definition for stock exchange

    Attributes:
    -----------
    name: str
        name of the stock exchange

    listedEquity: dict
        equity details listed on this exchange

    equityTransactions: defaultdict(list)
        transaction details(buy/sell) of the equities listed on this exchange
    '''

    
    def __init__(self, indexName="Simple Stock Exchange"):
        '''
        Parameters:
        ----------
        indexName: str, optional
            exchange name
        '''
        self.name = indexName
        self.listedEquity = dict()
        self.equityTransactions = defaultdict(list)
        self.__bootstrapListedStocks()
    
    
    def __bootstrapListedStocks(self):
        '''
        Bootstraping the exchange with equity and equity transaction details
        '''
        self.addStockToIndex(SimpleEquity(ticker='TEA', lastDividend=0, parValue=100, fixedDividend=0.0, type=EquityType.COMMON.value))
        self.addStockToIndex(SimpleEquity(ticker='POP', lastDividend=8, parValue=100, fixedDividend=0.0, type=EquityType.COMMON.value))
        self.addStockToIndex(SimpleEquity(ticker='ALE', lastDividend=23, parValue=60, fixedDividend=0.0, type=EquityType.COMMON.value))
        self.addStockToIndex(SimpleEquity(ticker='GIN', lastDividend=8, parValue=100, fixedDividend=0.02, type=EquityType.PREFERRED.value))
        self.addStockToIndex(SimpleEquity(ticker='JOE', lastDividend=13, parValue=250, fixedDividend=0.0, type=EquityType.COMMON.value))

        self.buyStock('TEA', 100, 1500)
        self.buyStock('TEA', 150, 1400)
        self.buyStock('POP', 100, 500)
        self.buyStock('ALE', 1000, 100)
        self.buyStock('GIN', 300, 2500)
        self.buyStock('JOE', 450, 700)
        self.buyStock('GIN', 140, 900)

        self.sellStock('TEA', 50, 1200)
        self.sellStock('POP', 150, 1100)
        self.sellStock('POP', 250, 1000)
        self.sellStock('ALE', 350, 200)
        self.sellStock('GIN', 250, 2200)
        self.sellStock('JOE', 150, 900)
        self.sellStock('JOE', 450, 1000)
        self.sellStock('ALE', 500, 200)

    
    def addStockToIndex(self, equity):
        '''
        Adding new equity fo the exchange

        Parameters:
        ----------
        equity: SimpleEquity
            equity object
        
        Raises:
        -------
        ValueError:
            If equity already exists in the exchange
        '''
        if not self.isStockListed(equity.ticker) and isinstance(equity, SimpleEquity):
            self.listedEquity[equity.ticker] = equity
        else:
            raise ValueError("Equity already exists in the exchange!")


    def buyStock(self, ticker, quantity, strikePrice):
        '''
        Buy an equity share and record the transaction

        Parameters:
        -----------
        ticker: str
            unique identifier for equity
        quantity: int
            number of units of share to buy
        strikePrice: float
            the price at which equity is being bought
        
        Raises:
        ------
        ValueError:
            If given ticker is not listed in the exchange
        '''
        if self.isStockListed(ticker):
            self.equityTransactions[ticker].append(self.getTransactionDetails(TransactionType.BUY.value, quantity, strikePrice))
        else:
            raise ValueError("Equity is not listed in this exchange!")


    def getGBCE(self):
        '''
        Calculates GBCE All share index 

        Returns:
        --------
        float
        '''
        transactions = self.getStockTransactions()
        prices = [i.get('StrikePrice') for i in transactions]
        return round(np.prod(prices)**(1/len(prices)), 2)


    def getStock(self, ticker):
        '''
        Given a equity ticker extracts equity details

        Parameters:
        ----------
        ticker: str
            unique identifier for equity
        
        Returns:
        -------
        SimpleEquity object

        Raises:
        -------
        ValueError:
            If given ticker is not listed in the exchange
        '''
        if self.isStockListed(ticker):
            return self.listedEquity.get(ticker)
        else:
            raise ValueError('Given stock is not listed')


    def getStockDetails(self):
        '''
        Lists all the equity details listed on the exchange

        Returns:
        list of dictionaries
        '''
        rslt = list()
        for i in self.listedEquity.values():
            rslt.append({
                'Ticker': i.ticker,
                'Type': i.type,
                'Last Dividend': i.lastDividend,
                'Fixed Dividend': i.fixedDividend,
                'Par Value': i.parValue
            })
        return rslt
    

    def getStockTransactions(self, ticker=None, inTimestamp=False):
        '''
        Lists all the transactions of all/specific ticker within the exchange

        Parameters:
        ----------
        ticker: str, optional
            unique identifier for equity

        inTimestamp: boolean
            to return the timestamp in date or timestamp format

        Returns:
        -------
        list of dictionaries

        Raises:
        ------
        ValueError:
            If given ticker is not listed in the exchange
        '''
        if ticker:
            ticker = ticker.upper()
            if self.isStockListed(ticker):
                rslt = list()
                for i in self.equityTransactions.get(ticker):
                    rslt.append({
                        'Ticker': ticker,
                        'TransactionType': i.get('transactionType'),
                        'TransactionDateTime': datetime.fromtimestamp(i.get('timestamp')) if not inTimestamp else i.get('timestamp'),
                        'Quantity': i.get('quantity'),
                        'StrikePrice': i.get('strikePrice')
                    })
                return rslt
            else:
                raise ValueError("Equity is not listed in this exchange!")
        else:
            rslt = list()
            for k, v in self.equityTransactions.items():
                rslt.extend([{'Ticker': k,
                    'TransactionType': i.get('transactionType'),
                    'TransactionDateTime': datetime.fromtimestamp(i.get('timestamp')),
                    'Quantity': i.get('quantity'),
                    'StrikePrice': i.get('strikePrice')} for i in v])
            return rslt


    def getTransactionDetails(self, transactionType, quantity, strikePrice):
        '''
        Prepared the transaction details

        Parameters:
        -----------
        transactionType: str
            buy/sell of the equity
        
        quantity: int
            number of units of share to buy/sell
        
        strikePrice: float
            the price at which equity is being bought/sold
        '''
        return {
            'transactionType': transactionType,
            'timestamp': time(),
            'quantity': quantity,
            'strikePrice': strikePrice
        }


    def getVolumeWeightedStockPrice(self, ticker):
        '''
        Calculate volume weighted stock price based on trades in past 15 minutes
        
        Parameters:
        ----------
        ticker: str
            unique identifier for equity

        Returns:
        -------
        float
        '''
        transactions = self.getStockTransactions(ticker, inTimestamp=True)
        timeCutOff = (datetime.fromtimestamp(time()) - timedelta(minutes=15)).timestamp()
        transactions = [i for i in transactions if i.get('TransactionDateTime')>=timeCutOff]
        num = 0
        deno = 0
        if transactions:
            for i in transactions:
                num += i.get('StrikePrice') * i.get('Quantity')
                deno += i.get('Quantity')
            return round(num/deno, 2)
        else:
            return 0


    def isStockListed(self, ticker):
        '''
        Checks if the ticker is listed in the exchange or not

        Parameters:
        ----------
        ticker: str
            unique identifier for equity
        '''
        return ticker.upper() in self.listedEquity.keys()


    def removeStockFromIndex(self, equity):
        '''
        Remove equity from exchange
        
        Parameters:
        ----------
        equity: SimpleEquity
            equity object
        
        Raises:
        -------
        ValueError:
            If equity does not exists in the exchange
        '''
        if self.isStockListed(equity.ticker) and isinstance(equity, SimpleEquity):
            self.listedEquity.pop(equity.ticker)
        else:
            raise ValueError("Equity does not exists in the exchange!")


    def sellStock(self, ticker, quantity, strikePrice):
        '''
        Sell an equity share and record the transaction

        Parameters:
        -----------
        ticker: str
            unique identifier for equity
        quantity: int
            number of units of share to sell
        strikePrice: float
            the price at which equity is being sold
        
        Raises:
        ------
        ValueError:
            If given ticker is not listed in the exchange
        '''
        if self.isStockListed(ticker):
            self.equityTransactions[ticker].append(self.getTransactionDetails(TransactionType.SELL.value, quantity, strikePrice))
        else:
            raise ValueError("Equity is not listed in this exchange!")