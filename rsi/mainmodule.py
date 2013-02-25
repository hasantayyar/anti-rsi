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
    operation = sys.argv[1]
    if operation == "start":
        dm.start()
    elif operation == "stop":
        dm.stop()

def log(msg):
    return msg

