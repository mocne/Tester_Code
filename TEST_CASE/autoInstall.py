# -*- coding: utf-8 -*-

import os

packageName = 'cn.phaidai.loan'
versionCmd = 'adb shell "dumpsys package ' + packageName + ' | grep versionName"'
pathCmd = './adb shell pm path ' + packageName
pathPesult = os.popen(pathCmd).read()
versionPesult = os.popen(versionCmd).read()
if pathPesult:
    print("App found on the device")
    if versionPesult:
        print(versionPesult)
    else:
        print("App not found on the device")
else:
    print("App not found on the device")

