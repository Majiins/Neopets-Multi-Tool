import time

class Snowager:
    def __init__(self, neo):
        self.neo = neo

    def doSnowager(self, username):
        run = self.neo.setData(username, 'snowager')
        if time.time() - float(run) >= 10800:
            resp = self.neo.get('winter/snowager2.phtml', 'http://www.neopets.com/winter/snowager.phtml')
            if resp.find('You dont want to try and enter again') < 0:
                gamePrize = self.neo.gameParse(resp, '<p><b>', '<p></center><center>')
                self.neo.log('Snowager: %s' % gamePrize)
            else:
                self.neo.log('Snowager: It\'s too early to visit yet')
            self.neo.updateData(username, 'snowager', '%s:%s' % ('snowager', time.time()))