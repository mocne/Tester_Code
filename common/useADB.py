# -*- coding: utf-8 -*-

import os
import platform

sysName = platform.system()

def getAppAutomate():
    top = os.path.abspath(os.path.dirname(os.getcwd()))
    appName = os.popen('ls ' + top + '/app/testingApp/*.apk').read()
    return appName

def justGetAppInfo():


    if sysName == 'Linux':

        app = getAppAutomate()
        tmp = os.popen('/opt/sdk/sdk/build-tools/android-4.4W/aapt dump badging %s' % app).read()

        packageNameEndNum = tmp.find('versionCode=') - 2
        packageName = tmp[15:packageNameEndNum]

        activityNameStartNum = tmp.find('launchable-activity') + 27
        activityNameEndNum = tmp.find('\'  label=\'')
        activityName = tmp[activityNameStartNum:activityNameEndNum]

        return packageName, activityName

def justCheckAppStatus():
    print('aaa')

def justGetDevicesInfo():
    deviceInfo = {}
    if sysName == 'Linux':
        a = os.getcwd()
        # 设备名
        DeviceName = os.popen('/opt/sdk/sdk/platform-tools/adb devices').read().split('\n')[1].split('\t')[0]
        deviceInfo['deviceName'] = DeviceName
        # 系统版本
        DeviceVersion = os.popen('/opt/sdk/sdk/platform-tools/adb shell getprop ro.build.version.release').read()
        deviceInfo['systemVersion'] = DeviceVersion[:-1]
        # 手机厂商  ‘adb -d shell getprop ro.product.brand’
        # 手机型号 ‘adb -d shell getprop ro.product.model’
        # 手机序列号 ‘adb get-serialno’
        # API版本  ‘adb shell getprop ro.build.version.sdk’
        # 获取手机内存信息 adb shell cat /proc/meminfo
        '''
        7、获取手机的IMEI
有三种方式，由于手机和系统的限制，不一定获取到
1、 adb shell dumpsys iphonesubinfo
  ● 1
其中Device ID即为IMEI号
2、 adb shell getprop gsm.baseband.imei
  ● 1
3、 service call iphonesubinfo 1 
  ● 1
此种方式，需要自己处理获取的信息得到
8、获取手机mac地址

adb shell cat /sys/class/net/wlan0/address
  ● 1
  ● 2
9、获取手机内存信息
adb shell cat /proc/meminfo
  ● 1
10、获取手机存储信息
adb shell df
  ● 1
获取手机内部存储信息：
魅族手机： adb shell df /mnt/shell/emulated
  ● 1
其他： adb shell df /data
  ● 1
获取sdcard存储信息：
adb shell df /storage/sdcard
  ● 1
11、获取手机分辨率
adb shell "dumpsys window | grep mUnrestrictedScreen"
  ● 1
12、获取手机物理密度
adb shell wm density
        '''
        print('')

if __name__ == '__main__':
    PN, AN = justGetAppInfo()
    print(PN)
    print(AN)
    justGetDevicesInfo()
