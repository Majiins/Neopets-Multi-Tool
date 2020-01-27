import requests
import os
import time
import random
import fileinput
import sys

class neo:
    def __init__(self):
        self.s = requests.session()
        self.base = 'http://www.neopets.com/'
        self.useragent = None
        self.minDelay = None
        self.maxDelay = None
        self.getSettings()
        self.setHeaders()

    def url(self, path):
        return '%s%s' % (self.base, path)

    def getBetween(self, data, first, last):
        ''' returns data between two strings. For example:
            data = 'abcdefg'
            first = 'abc'
            last = 'efg'
            returns: 'd' '''
        return data[data.find(first) + len(first):data.find(last)]

    def log(self, msg):
        ''' formats the print function to display
            the current date & time the message
            was added to the console '''
        print(time.strftime('%A') + ' ' + '%s%s' %(time.strftime('%H:%M:%S => '),msg.encode('utf-8').decode('utf-8')))

    def proxy(self, prox):
        ''' Sets the connection to tunnel through a proxy
            only http is listed since neopets only uses http
            for whatever reason '''
        self.s.proxies.update({'http': 'http://%s' % prox})

    def getSettings(self):
        ''' Sets the useragent, minDelay, maxDelay to
            the values that have been set in settings > settings.txt '''
        with open('settings/settings.txt', 'r') as f:
            settings = f.read().rstrip()
        bot = self.getBetween(settings, '[bot]', '[/bot]')
        bot = bot.split('\n')[1:-1]
        self.useragent = bot[0].split(':', 1)[1].strip()
        self.minDelay = float(bot[1].split(':', 1)[1].strip())
        self.maxDelay = float(bot[2].split(':', 1)[1].strip())

    def setHeaders(self):
        ''' Sets the required headers needed to get/post requests
            to neopets '''
        self.s.headers.update({'User-Agent': self.useragent, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9'})
    
    def updateData(self, username, task, data):
        for line in fileinput.input(['data/%s' % username], inplace=True):
            if line.strip().startswith(task):
                line = '%s\n' % (data)
            sys.stdout.write(line)

    def setData(self, username, task):
        if username not in os.listdir('data'):
            with open('data/%s' % username, 'w') as f:
                f.write('')
        with open('data/%s' % (username), 'r') as f:
            if task not in f.read():
                with open('data/%s' % username, 'a') as f:
                    f.write('%s:0' % (task))
                with open('data/%s' % username, 'r') as f:
                    for data in f:
                        tasks = data.split(':')
                        if tasks[0] == task:
                            return tasks[1]
                return False
            else:
                with open('data/%s' % username, 'r') as f:
                    for data in f:
                        tasks = data.split(':')
                        if tasks[0] == task:
                            return tasks[1]
                return False

    def get(self, path, referer = None):
        time.sleep(random.uniform(self.minDelay, self.maxDelay))
        if referer:
            self.s.headers.update({'Referer': referer})
        url = self.url(path)
        r = self.s.get(url)
        if 'Referer' in self.s.headers:
            del self.s.headers['Referer']
        return r.text

    def post(self, path, data, referer = None):
        time.sleep(random.uniform(self.minDelay, self.maxDelay))
        if referer:
            self.s.headers.update({'Referer': referer})
        url = self.url(path)
        if data:
            r = self.s.post(url, data=data)
        else:
            r = self.s.post(url)
        return r.text