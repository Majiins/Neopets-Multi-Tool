import time
import json

class Trudy:
    def __init__(self, neo):
        self.neo = neo

    def doTrudy(self, username):
        run = self.neo.setData(username, 'trudy')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('trudys_surprise.phtml?delevent=yes')
            if resp.find('&slt=1') > 1:
                result = self.neo.getBetween(resp, '/trudydaily/slotgame.phtml?id=', '" name="')
                resp = self.neo.get('trudydaily/slotgame.phtml?id=%s' % result, 'http://www.neopets.com/trudys_surprise.phtml?delevent=yes')
                results = self.neo.getBetween(resp, '\'key\': \'', '\'};')
                self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'getslotstate', 'key': results}, 'http://www.neopets.com/trudydaily/slotgame.phtml?id=%s' % result)
                resp = self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'beginroll'}, 'http://www.neopets.com/trudydaily/ajax/claimprize.php')
                for x in json.loads(resp)['prizes']:
                    self.neo.log('Trudy\'s Surprise: Won %sNP!' % x['value'])
                self.neo.post('trudydaily/ajax/claimprize.php', {'action': 'prizeclaimed'}, 'http://www.neopets.com/trudydaily/ajax/claimprize.php')
                self.neo.updateData(username, 'trudy', '%s:%s' % ('trudy', time.time()))
        else:
            self.neo.log('Already Done Trudy\'s Surprise Today')