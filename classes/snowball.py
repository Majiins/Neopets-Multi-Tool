from classes.deposit import SDB
import time

class Snowball:
    def __init__(self, neo):
        self.neo = neo
        self.deposit = SDB(self.neo)

    def doSnowball(self, username):
        run = self.neo.setData(username, 'snowball')
        if time.time() - float(run) >= 1800:
            resp = self.neo.post('faerieland/springs.phtml', {'type': 'purchase'}, 'http://www.neopets.com/faerieland/springs.phtml')
            if resp.find('buy one item every 30 minutes') > 1:
                self.neo.log('Snowball AB: Can\'t Buy A Snowball Yet!')
            else:
                self.neo.get('faerieland/process_springs.phtml?obj_info_id=8429', 'http://www.neopets.com/faerieland/springs.phtml')
                self.neo.log('Snowball AB: Purchased x1 Sticky Snowball')
                self.deposit.doDeposit()
            self.neo.updateData(username, 'snowball', '%s:%s' % ('snowball', time.time()))