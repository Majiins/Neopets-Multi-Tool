import re

class SDB:
    def __init__(self, neo):
        self.neo = neo

    def doDeposit(self):
        arr = 1
        resp = self.neo.get('quickstock.phtml', 'http://www.neopets.com/inventory.phtml')
        items = "<TD align=\"left\">"
        results = resp.count(items)
        if results:
            item_ids = re.findall('value="(.*)"><TD', resp)
            data = {}
            data['buyitem'] = 0
            for item in item_ids:
                data['id_arr[%s]' % arr] = item
                data['radio_arr[%s]' % arr] = 'deposit'
                arr += 1
            data['checkall'] = 'on'
            self.neo.post('process_quickstock.phtml', data, 'http://www.neopets.com/quickstock.phtml')
        if results:
            self.neo.log('Cleaned Inventory')