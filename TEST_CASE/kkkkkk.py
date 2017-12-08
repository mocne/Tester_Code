# -*- coding: utf-8 -*-

import os

port = 4723
pidStr = 'netstat -ano | findstr ' + str(port)
pidNum = os.popen(pidStr).read().split(' ')[-1][:-1]
if pidNum:
    kiStr = 'taskkill -PID ' + pidNum + ' -F'
    killServer = os.popen(kiStr).read()[:2]
    if killServer == '成功':
        print('Kill ' + str(port) + 'success')
    else:
        print('Kill ' + str(port) + 'fail')
else:
    print('Useless pidNum')