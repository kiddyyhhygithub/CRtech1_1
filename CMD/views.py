from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse
# Create your views here.
import os
import yh.hy.IoTUtility.IoT as iotut
import yh.hy.Const.IoTConst as iotconst
from django.core.cache import cache
import json
import threading
from concurrent.futures import ThreadPoolExecutor
def cmd(request):

    # jsonPath = os.path.join(settings.CA_ROOT, r'body.txt')
    # with open(jsonPath,'a+') as f:
    #     f.writelines(str(request.body) + '\n')

    # jsonPath1 = os.path.join(settings.CA_ROOT, r'bodydecode.txt')

    # return HttpResponse('finish')
    # return HttpResponse(request.body.decode('utf-8'))

    # body = request.body
    # print(body)
    # bodyStr = json.loads(body)
    # try:
    #     bodyStr = json.loads(body)
    # except:
    #     pass
    # try:
    #     bodyStr = json.loads(body.decode('utf-8'))
    # except:
    #     pass


    # return HttpResponse(str( bodyStr))
    # jsonPath = os.path.join(settings.CA_ROOT, r'body.txt')
    # with open(jsonPath,'a+') as f:
    #     f.writelines(bodyStr + '\n')
    # with open(os.path.join(settings.CA_ROOT,'log.ini'),'a+') as f:
    #     f.writelines(str( request.body) + '\n')
    # return HttpResponse('write ok')
    bodyStr = json.loads( request.body.decode('utf-8') )
    protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
    print(protocol)
    # return HttpResponse(protocol)
    if protocol != 'NF0000442':
        return HttpResponse('ERR0')
    ca = (
        os.path.join(settings.CA_ROOT,r'server.crt'),
        os.path.join(settings.CA_ROOT, r'server.key'),
    )
    token = cache.get('token')

    appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
    secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
    iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)#必须要放if外面，否则会报错


    if token==None:

        token = iot.getToken()
        cache.set('token',token,60*30)
        filePath = os.path.join(settings.CA_ROOT,r'token_his.extend')
        with open(filePath,'a+') as f:
            f.writelines(token + '\n')

    print('token',token)
    deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'
    serviceId = r'ZmSer'
    method = r'CMD'
    cmdValue = r'A00000'

    #是否是立即下发
    EXPIRETIME = 0

    #是否需要用线程池

    #使用普通线程

    local.cmdcode = None
    local.cmdinf = None
    # cmdcode,cmdinf = iot.CMD(_token=token,
    #         _deviceId=deviceId,
    #         _serviceId=serviceId,
    #         _method=method,
    #         _cmdvalue=cmdValue,
    #         _expireTime=EXPIRETIME,
    #         _callbackUrl=None)
    threading.Thread(target=threadCMD(_token=token,
            _deviceId=deviceId,
            _serviceId=serviceId,
            _method=method,
            _cmdvalue=cmdValue,
            _expireTime=EXPIRETIME,
            _callbackUrl=None)).start()
    cmdcode, cmdinf = local.cmdcode,local.cmdinf


    iot = None
    return HttpResponse(cmdcode,cmdinf)
local = threading.local()

def threadCMD(_token,
            _deviceId,
            _serviceId,
            _method,
            _cmdvalue,
            _expireTime,
            _callbackUrl):
    local.cmdcode, local.cmdinf = iotut.IoT.CMD(_token=_token,
            _deviceId=_deviceId,
            _serviceId=_serviceId,
            _method=_method,
            _cmdvalue=_cmdvalue,
            _expireTime=_expireTime,
            _callbackUrl=_callbackUrl)

    pass