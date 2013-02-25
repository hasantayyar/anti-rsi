#!/usr/bin/env python
import sys, time
from daemon import Daemon

class rsidaemon(Daemon):
    def run(self):
        while True:
            log("keep running")
            time.sleep(1)
if __name__ == '__main__':
    dm = rsidaemon("/tmp/anti-rsi.pid")
    dm.start()

def log(msg):
    return msg

