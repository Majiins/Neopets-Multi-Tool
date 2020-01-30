import time, re

class Stocks:
    def __init__(self, neo):
        self.neo = neo

    def doStocks(self, username):
        run = self.neo.setData(username, 'stocks')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('stockmarket.phtml?type=list&full=true', 'http://www.neopets.com/stockmarket.phtml?type=buy')
            data = 15
            tryAgain = 15
            for _ in range(3):
                stock = list(set(re.findall('<b>(\w+?) %s [-\+]\d+?<\/b>' % data, resp)))
                if not stock:
                    tryAgain += 1
                    self.neo.log('Stock Buyer: No stocks for %s found, trying %s..' % (data, tryAgain))
                    data += 1
                if stock:
                    resp = self.neo.get('stockmarket.phtml?type=buy', 'http://www.neopets.com/stockmarket.phtml?type=list&full=true')
                    stockHash = self.neo.gameParse(resp, '&_ref_ck=', '\';')
                    resp = self.neo.post('process_stockmarket.phtml', {'_ref_ck': stockHash, 'type': 'buy', 'ticker_symbol': stock[0], 'amount_shares': '1000'}, 'http://www.neopets.com/stockmarket.phtml?type=buy')
                    if resp.find('purchase limit of 1000') > 1:
                        self.neo.log('Stock Buyer: You can\'t buy more than 1000 shares per day')
                    if resp.find('You cannot afford') > 1:
                        self.neo.log('Stock Buyer: You don\'t have enough neopoints')
                    if resp.find('purchase limit of 1000') < 0:
                        if resp.find('You cannot afford') < 0:
                            self.neo.log('Stock Buyer: Purchased 1000 shares of %s for %s' % (stock[0], data))
                    break
            self.neo.updateData(username, 'stocks', '%s:%s' % ('stocks', time.time()))
