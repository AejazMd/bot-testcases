
import pandas as pd
from modules.exchange import SimpleStockExchange


def assignmentOptions():
    '''
    Menu for selection of options
    '''
    print("*********************************")
    print("1 : Calculate Dividend Yield")
    print("2 : Calculate P/E Ratio")
    print("3 : Buy/Sell a stock")
    print("4 : Calculate volume weighted stock price")
    print("5 : Calculate GBCE Index")
    print("6 : List all stocks")
    print("7 : List all stock transactions")
    print("8 : Exit")
    print("*********************************")


def getStockFromTicker(se):
    '''
    Requests input ticker to be checked in the exchange listings

    Parameters:
    -----------
    se: SimpleStockExchange

    Returns:
    -------
    SimpleEquity
    '''
    ticker = input("Provide stock ticker: ")
    stock = se.getStock(ticker.upper())
    return stock


def getStockTickerAndPrice(se):
    '''
    Requests input ticker & price to be checked in the exchange listings

    Parameters:
    -----------
    se: SimpleStockExchange

    Returns:
    -------
    SimpleEquity, float
    '''
    stock = getStockFromTicker(se)
    price = float(input("Provide stock price: "))
    if price<=0:
        raise ValueError("Stock price should be more than zero!")
    return stock, price


def runAssignment():
    '''
    Initializes the stock exchange and executes all the options as per user request

    Raises:
    ------
    ValueError:
        If any error is encountered
    '''
    se = SimpleStockExchange()
    while True:
        assignmentOptions()
        option = input("select from above options: ")

        try:
            if option == "1":
                stock, price = getStockTickerAndPrice(se)
                print("Dividend Yield for %s=%s"%(stock.ticker, stock.getDividendYield(price)))

            elif option == "2":
                stock, price = getStockTickerAndPrice(se)
                print("P/E Ratio for %s:%s"%(stock.ticker, stock.getPriceToEarningsRatio(price)))

            elif option == "3":
                isBuy = input("buy(b) or sell(s)?: ")
                if isBuy == "b":
                    stock, price = getStockTickerAndPrice(se)
                    quantity = int(input("How many stock you want to buy: "))
                    se.buyStock(stock.ticker, quantity, price)
                    print("Bought %s stocks of %s at %s strike price"%(quantity, stock.ticker, price))
                elif isBuy == "s":
                    stock, price = getStockTickerAndPrice(se)
                    quantity = int(input("How many stock you want to sell: "))
                    se.sellStock(stock.ticker, quantity, price)
                    print("Sold %s stocks of %s at %s strike price"%(quantity, stock.ticker, price))
                else:
                    print("Incorrect option!")

            elif option == "4":
                stock = getStockFromTicker(se)
                print("Volume weighted stock price in past 15 mins for %s: %s"%(stock.ticker, se.getVolumeWeightedStockPrice(stock.ticker)))

            elif option == "5":
                print("GBCE all share index: ", se.getGBCE())

            elif option == "6":
                print("Listed stocked in exchange: %s"%(se.name))
                df = pd.DataFrame(se.getStockDetails())
                print(df)

            elif option == "7":
                print("Listed stocked transaction in exchange: %s"%(se.name))
                df = pd.DataFrame(se.getStockTransactions())
                print(df)

            elif option == "8":
                break
            else:
                print("Invalid option given")
        except ValueError as e:
            print("Error Encountered:", e)


if __name__ == "__main__":
    runAssignment()