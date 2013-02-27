#!/usr/bin/env python
import sys, time
from daemon import Daemon
import time
import datetime


class rsidaemon(Daemon):
    def run(self):
        while True:
            import osxnotification
            now = datetime.datetime.now()
            m = now.minute
            msg = False
            if m % 10 == 0:
                msg = "Hands up for one minute!"
            elif m % 30 == 0:
                msg = "Arm exercises for 2 minute!"
            if msg:
                osxnotification.notify("RSI ALERT!", "time for break!", msg)
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

