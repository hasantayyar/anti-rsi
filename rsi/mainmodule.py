#!/usr/bin/env python
import sys, time
from daemon import Daemon

class rsidaemon(Daemon):
    def run(self):
        while True:
            print("keep going")
            time.sleep(1)
        print("something about notification")

if __name__ == '__main__':
    dm = rsidaemon("/tmp/anti-rsi.pid")
    dm.start()

