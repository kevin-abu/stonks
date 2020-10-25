"""
Run stocks("ticker of stock in PSE")
    ex. stock("FLI")
"""

import webbrowser

def stock(ticker):
    url = 'https://www.investagrams.com/Stock/PSE:REPLACE'
    stockJockey = 'https://www.investagrams.com/StockJockey/?stock=PSE:REPLACE'
    Posts = 'https://www.investagrams.com/Search/All/PSE:REPLACE'

    webbrowser.get(chrome_path).open(url.replace("REPLACE", ticker))
    webbrowser.get(chrome_path).open(stockJockey.replace("REPLACE", ticker))
    webbrowser.get(chrome_path).open(Posts.replace("REPLACE", ticker))
    
