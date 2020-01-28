import time

class Bank:
    def __init__(self, neo):
        self.neo = neo

    def doInterest(self, username):
        run = self.neo.setData(username, 'bank')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('bank.phtml', 'https://www.jellyneo.net/?go=dailies')
            if resp.find('I see you don\'t currently have an account with us.') > 1:
                self.neo.log('Bank Interest: You don\'t have a bank account')
                self.neo.updateData(username, 'bank', '%s:%s' % ('bank', time.time()))
                return False
            if resp.find('You have already collected your interest today.') < 0:
                bankInterest = self.neo.gameParse(resp, 'gain <b>', ' NP</b>')
                self.neo.post('process_bank.phtml', {'type': 'interest'}, 'http://www.neopets.com/bank.phtml')
                self.neo.log('Bank Interest: Collected %s NP!' % bankInterest)
            else:
                self.neo.log('Bank Interest: You have already collected your interest today')
            self.neo.updateData(username, 'bank', '%s:%s' % ('bank', time.time()))