#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Project : IotUtility
# @FileName: run.py
# @Time  : 2019/7/13 9:57
# @Author : 颜华
#@Email : kiddyflash@163.com

import yh.hy.IoTUtility.IoT as iot
import os

def main():

    iot_class = iot.IoT()


    # workPath = os.path.join('./cert')
    # certFilePath = os.path.join(workPath, 'server.crt')
    # certFilePath1 = os.path.join(workPath, 'server.key')
    # cert = (certFilePath, certFilePath1)

    iot_class.test('yanhua')

    return None


if __name__ == '__main__':
    main()