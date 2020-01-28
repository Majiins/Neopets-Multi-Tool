import time

class Apple:
    def __init__(self, neo):
        self.neo = neo

    def doApple(self, username):
        run = self.neo.setData(username, 'apple')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get
            resp = self.neo.get('halloween/applebobbing.phtml?bobbing=1', 'http://www.neopets.com/halloween/applebobbing.phtml')
            if resp.find('Think I\'m blind underneath this hat?') > 1:
                self.neo.log('Apple Bobbing: Already played today')
                self.neo.updateData(username, 'apple', '%s:%s' % ('apple', time.time()))
                return False
            if resp.find('I mean, bully for you!') > 1:
                gamePrize = self.neo.gameParse(resp, '<br><b>', '</b></center>')
                self.neo.log('Apple Bobbing: Won %s' % gamePrize)
            else:
                self.neo.log('Apple Bobbing: Didn\'t Win A Prize')
            self.neo.updateData(username, 'apple', '%s:%s' % ('apple', time.time()))