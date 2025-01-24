from enum import Enum

class EquityType(Enum):
    '''
    Constants for equity type
    '''
    COMMON = "common"
    PREFERRED = "preferred "


class TransactionType(Enum):
    '''
    Constants for transaction type
    '''
    BUY = "buy"
    SELL = "sell"