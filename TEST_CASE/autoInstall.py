# -*- coding: utf-8 -*-

import os
import time
import common.useADB

packageName = common.useADB.justGetAppInfo()[0]
versionCmd = 'adb shell "dumpsys package ' + packageName + ' | grep versionName"'
pathCmd = 'adb shell pm path ' + packageName
pathResult = os.popen(pathCmd).read()

def autoInstallApp():

    if pathResult:
        print("App found on the device")
        versionResult = os.popen(versionCmd).read().split('=')[1]
        if versionResult:
            print(versionResult)
        else:
            print("App version info not found on the device")
    else:
        print("App not found on the device")
        top = os.path.abspath(os.path.dirname(os.getcwd())).replace('\\', '/')
        appPath = os.popen('ls ' + top + '/app/testingApp/*.apk').read()[:-1]
        appName = os.popen('ls ' + top + '/app/testingApp/').read()[:-1]
        print(top)
        cmdStr = 'adb push ' + appPath + ' /sdcard/' + appName
        os.popen('adb remount')
        pushResult = os.popen(cmdStr).read()
        time.sleep(5)
        os.popen('adb shell pm install /sdcard/' + appName)
        # installInfo = os.popen('adb install -r /system/app/' + appName).read()
        # print('install: ' + installInfo)

def autoUnInstallApp():
    if pathResult:
        os.popen('adb uninstall ' + packageName)
        print('aaaaaaaaaassssssssssssssss')

if __name__ == '__main__':
    autoInstallApp()
    # autoUnInstallApp()