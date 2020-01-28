import time

class Anchor:
    def __init__(self, neo):
        self.neo = neo

    def doAnchor(self, username):
        run = self.neo.setData(username, 'anchor')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('pirates/anchormanagement.phtml', 'http://www.jellyneo.net/index.php/?go=dailies')
            if resp.find('free to come back tomorrow') > 1:
                self.neo.log('Anchor Management: Already played today')
                self.neo.updateData(username, 'anchor', '%s:%s' % ('anchor', time.time()))
                return False
            gameHash = self.neo.gameParse(resp, '"hidden" value="', '"></form>')
            resp = self.neo.post('pirates/anchormanagement.phtml', {'action': gameHash}, 'http://www.neopets.com/pirates/anchormanagement.phtml')
            gamePrize = self.neo.gameParse(resp, '-name">', '<')
            self.neo.log('Anchor Management: The krawken leaves you %s' % gamePrize)
            self.neo.updateData(username, 'anchor', '%s:%s' % ('anchor', time.time()))