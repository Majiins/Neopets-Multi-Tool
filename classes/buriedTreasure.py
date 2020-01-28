import time
from random import randint

class Buried:
    def __init__(self, neo):
        self.neo = neo

    def doTreasure(self, username):
        run = self.neo.setData(username, 'treasure')
        if time.time() - float(run) >= 10800:
            resp = self.neo.get('pirates/buriedtreasure/buriedtreasure.phtml?', 'https://www.jellyneo.net/?go=dailies')
            if resp.find('you have to wait another') < 0:
                x, y = randint(25, 450), randint(45, 460)
                resp = self.neo.get('pirates/buriedtreasure/buriedtreasure.phtml?%s,%s' % (x, y), 'http://www.neopets.com/pirates/buriedtreasure/buriedtreasure.phtml?')
                gamePrize = self.neo.gameParse(resp, '<b><center>', '</center></b>')
                self.neo.log('Buried Treasure: %s' % gamePrize)
            self.neo.updateData(username, 'treasure', '%s:%s' % ('treasure', time.time()))