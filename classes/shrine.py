import time

class Shrine:
    def __init__(self, neo):
        self.neo = neo

    def doShrine(self, username):
        run = self.neo.setData(username, 'shrine')
        if time.time() - float(run) >= 46800:
            resp = self.neo.post('desert/shrine.phtml', {'type': 'approach'}, 'http://www.neopets.com/desert/shrine.phtml')
            if resp.find('Maybe you should wait') > 1:
                self.neo.log('Coltzan\'s Shrine: Maybe you should wait a while before visiting the shrine again....')
                self.neo.updateData(username, 'shrine', '%s:%s' % ('shrine', time.time()))
                return False
            if resp.find('Awww, nothing happened.') < 0:
                gamePrize = self.neo.gameParse(resp, '</b><p>', '</p>')
                self.neo.log('Coltzan\'s Shrine: %s' % gamePrize)
            else:
                self.neo.log('Coltzan\'s Shrine: Nothing Happened')
            self.neo.updateData(username, 'shrine', '%s:%s' % ('shrine', time.time()))