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
            s = now.second
            msg = False
            notif_showed = False
            if m % 10 == 0 and s < 2:
                msg = "Hands up for one minute!"
                if notif_showed == False:
                    notif_showed = True
            elif m % 30 == 0 and s < 2:
                msg = "Arm exercises for 2 minute!"
                if notif_showed == False:
                    notif_showed = True
            else:
                notif_showed = False
            if msg and  notif_showed:
                notif_showed = True
                osxnotification.notify("RSI ALERT!", "time for break!", msg)
            time.sleep(1)
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

