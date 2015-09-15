#!/usr/bin/env python
# encoding: utf-8

import threading
def worker(number):
    print 'worker: %s' % number
    return

for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()
