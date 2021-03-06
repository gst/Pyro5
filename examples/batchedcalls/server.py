import time
from Pyro5.api import expose, Daemon


@expose
class Thingy(object):
    def multiply(self, a, b):
        return a * b

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a // b

    def error(self):
        return 1 // 0

    def delay(self, seconds):
        time.sleep(seconds)
        return seconds

    def printmessage(self, message):
        print(message)
        return 0


Daemon.serveSimple({
    Thingy: "example.batched"
}, ns=False)
