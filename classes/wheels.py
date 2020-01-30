import time

class Wheels:
    def __init__(self, neo):
        self.neo = neo

    def wheelExcitement(self, username):
        run = self.neo.setData(username, 'excitement')
        if time.time() - float(run) >= 7200:
            resp = self.neo.get('faerieland/wheel.phtml', 'http://www.jellyneo.net/?go=dailies')
            if resp.find('Already spun') < 0:
                resp = self.neo.amf('\x00\x03\x00\x00\x00\x01\x00\x16WheelService.spinWheel\x00\x02/1\x00\x00\x00\t\n\x00\x00\x00\x01\x02\x00\x01' + '2')
                self.neo.log('Wheel of Excitement: Done')
            self.neo.updateData(username, 'excitement', '%s:%s' % ('excitement', time.time()))

    def wheelExtravagance(self, username):
        run = self.neo.setData(username, 'extravagance')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('desert/extravagance.phtml', 'http://www.jellyneo.net/?go=dailies')
            if resp.find('Already spun') < 0:
                resp = self.neo.amf('\x00\x03\x00\x00\x00\x01\x00\x16WheelService.spinWheel\x00\x02/1\x00\x00\x00\t\n\x00\x00\x00\x01\x02\x00\x01' + '6')
                self.neo.log('Wheel of Extravagance: Done')
            self.neo.updateData(username, 'extravagance', '%s:%s' % ('extravagance', time.time()))

    def wheelMediocrity(self, username):
        run = self.neo.setData(username, 'mediocrity')
        if time.time() - float(run) >= 2400:
            resp = self.neo.get('prehistoric/mediocrity.phtml', 'http://www.jellyneo.net/?go=dailies')
            if resp.find('Already spun') < 0:
                resp = self.neo.amf('\x00\x03\x00\x00\x00\x01\x00\x16WheelService.spinWheel\x00\x02/1\x00\x00\x00\t\n\x00\x00\x00\x01\x02\x00\x01' + '3')
                self.neo.log('Wheel of Mediocrity: Done')
            self.neo.updateData(username, 'mediocrity', '%s:%s' % ('mediocrity', time.time()))

    def wheelMisfortune(self, username):
        run = self.neo.setData(username, 'misfortune')
        if time.time() - float(run) >= 7200:
            resp = self.neo.get('halloween/wheel/index.phtml', 'http://www.jellyneo.net/?go=dailies')
            if resp.find('Already spun') < 0:
                resp = self.neo.amf('\x00\x03\x00\x00\x00\x01\x00\x16WheelService.spinWheel\x00\x02/1\x00\x00\x00\t\n\x00\x00\x00\x01\x02\x00\x01' + '4')
                self.neo.log('Wheel of Misfortune: Done')
                self.neo.updateData(username, 'misfortune', '%s:%s' % ('misfortune', time.time()))

    def wheelKnowledge(self, username):
        run = self.neo.setData(username, 'knowledge')
        if time.time() - float(run) >= 86400:
            resp = self.neo.get('medieval/knowledge.phtml', 'http://www.jellyneo.net/?go=dailies')
            if resp.find('Already spun') < 0:
                resp = self.neo.amf('\x00\x03\x00\x00\x00\x01\x00\x16WheelService.spinWheel\x00\x02/1\x00\x00\x00\t\n\x00\x00\x00\x01\x02\x00\x01' + '1')
                self.neo.log('Wheel of Knowledge: Done')
            self.neo.updateData(username, 'knowledge', '%s:%s' % ('knowledge', time.time()))