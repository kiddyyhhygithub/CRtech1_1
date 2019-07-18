#!/usr/bin/python3.7.2
# -*- coding: utf-8 -*-
# @Project : IotUtility
# @FileName: IoT.py
# @Time  : 2019/7/13 9:00
# @Author : 颜华
#@Email : kiddyflash@163.com
import os
import requests
import json
class IoT(object):

    def __init__(self,_baseurl='https://180.101.147.89',_port=8743,_appid=None,_secret=None,_cert=None):
        '''
        IoT基本操作类
        :param _baseurl: iot的主IP地址，如https://180.101.147.89
        :param _port: 端口号，int型
        :param _appid: AppID
        :param _secret: Secret
        :param _cert: 证书，元组类型 （cert1.crt,cert2.key）,元祖里面放两个证书路径
        '''
        self.baseurl = _baseurl + ':' + str(_port)
        self.appid = _appid
        self.secret = _secret
        self.cert = _cert
        pass

    def getToken(self):
        '''
        获取Token值
        :return:返回token字符串
        '''
        # workPath = os.path.join('./cert')
        # certFilePath = os.path.join(workPath, 'server.crt')
        # certFilePath1 = os.path.join(workPath, 'server.key')
        # cert = (certFilePath, certFilePath1)
        # cert = ('./cert/server.crt',
        #         './cert/server.key')
        token = None
        try:
            # request = requests.Session()
            # request.mount('https://', HTTPAdapter(pool_connections=11, pool_maxsize=11))
            url = self.baseurl + '/iocm/app/sec/v1.1.0/login'
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            # appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
            # secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'

            payload = {
                # 'appId': 'OXfN9xuxsCSfUN4h9Jjfzd9a14oa',
                # 'secret': 'kZU4W3lLgqg4DdBMUqccSppK2jQa'
                'appId': self.appid,
                'secret': self.secret,
            }
            # response = request.post(url, headers=headers, data=payload, cert=cert, verify=False, timeout=10)
            requests.packages.urllib3.disable_warnings()
            response = requests.post(url, headers=headers, data=payload, cert=self.cert, verify=False)
            print(response.status_code)
            print(response.text)
            token = json.loads(response.text)

        except Exception as ex:
            print(ex)

        # print(cert)
        return token['accessToken']
        return

    def CMD(self,_token,_deviceId,_serviceId,_method,_cmdvalue,_expireTime,_callbackUrl):
        '''
        向设备下发单个命令
        :param _token: token值
        :param _deviceId: 设备ID
        :param _serviceId: 下发命令的 服务ID
        :param _method: 下发的命令名
        :param _cmdvalue: 下发的值，根据profile来决定其类型
        :param _expireTime: 命令缓存时间，int型。0表示立即下发
        :param _callbackUrl:回调地址
        :return:返回平台给的信息,元组类型，（code,info）。code:状态码int；info:具体信息string
        '''
        url = self.baseurl + '/iocm/app/cmd/v1.4.0/deviceCommands'
        headers = {'Content-Type': 'application/json',
                   'app_key': self.appid,
                   'Authorization': 'Bearer ' + _token
                   }
        body = {"deviceId": _deviceId,
                "command": {
                    "serviceId": _serviceId,
                    "method": _method,
                    "paras": {
                        "cmdValue": _cmdvalue}
                },
                "expireTime": _expireTime,
                "callbackUrl": _callbackUrl
                }
        payload = json.dumps(body)
        requests.packages.urllib3.disable_warnings()
        result = requests.post(url=url, data=payload, verify=False, cert=self.cert, headers=headers)
        code = result.status_code
        info = result.text
        # print(result.status_code)
        # print(result.text)
        return (code,info)


    def CMDtest(self,_token,_deviceId,_serviceId,_method,_cmdvalue,_expireTime,_callbackUrl):
        cert = ('./cert/server.crt',
                './cert/server.key')
        url = self.baseurl + '/iocm/app/cmd/v1.4.0/deviceCommands'
        appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
        secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'

        # deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'
        # serviceId = r'ZmSer'
        # method = r'CMD'
        # methodValue = r'2726'
        url = r'https://180.101.147.89:8743/iocm/app/cmd/v1.4.0/deviceCommands'

        # token = '7a1e3b1632dfd6e1a7387e49594adca6'
        # token = r'9fc84d48259123c8a6868f1d59438db8'
        # print('token: ', _token)

        headers = {'Content-Type': 'application/json',
                   'app_key': self.appid,
                   'Authorization': 'Bearer ' + _token
                   }
        body = {"deviceId": _deviceId,
                "command": {
                    "serviceId": _serviceId,
                    "method": _method,
                    "paras": {
                        "cmdValue": _cmdvalue}
                },
                "expireTime": _expireTime,
                # "callbackUrl": "http://106.52.243.38/callback/"
                "callbackUrl":_callbackUrl
                }
        payload = json.dumps(body)
        result = requests.post(url=url, data=payload, verify=False, cert=self.cert, headers=headers)
        print(result.status_code)
        print(result.text)






    def test(self,_valStr):
        path = os.getcwd() + '/2.txt'
        with open(path,'a+') as f:
            f.writelines(_valStr + '\n')
        return None

    def test1(self):
        print(os.path.abspath('..'))

    def test2(self):
        print(os.getcwd())