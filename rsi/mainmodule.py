#!/usr/bin/env python
import sys, time
from daemon import Daemon
import osxnotification
import time


class rsidaemon(Daemon):
    def run(self):
        while True:
            osxnotification.notify("RSI ALERT!", "time for break!", 'lorem ipsum dolor sit amet lorem ipsum bla bla' )
            time.sleep(10)
if __name__ == '__main__':
    main()
def main():
    dm = rsidaemon("/tmp/anti-rsi.pid")
    operation = sys.argv[1]
    if operation == "start":
        dm.start()
    elif operation == "stop":
        dm.stop()

def log(msg):
    return msg

