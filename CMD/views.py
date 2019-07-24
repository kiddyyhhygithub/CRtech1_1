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

local = threading.local()

def cmd(request):
    local.cmdcode = None
    local.cmdinf = None
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
    # bodyStr = json.loads( request.body.decode('utf-8') )
    # protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
    # print(protocol)
    # # return HttpResponse(protocol)
    # if protocol != 'NF0000442':
    #     return HttpResponse('ERR0')
    # ca = (
    #     os.path.join(settings.CA_ROOT,r'server.crt'),
    #     os.path.join(settings.CA_ROOT, r'server.key'),
    # )
    # token = cache.get('token')
    #
    # appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
    # secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
    # iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)#必须要放if外面，否则会报错
    #
    #
    # if token==None:
    #
    #     token = iot.getToken()
    #     cache.set('token',token,60*30)
    #     filePath = os.path.join(settings.CA_ROOT,r'token_his.extend')
    #     with open(filePath,'a+') as f:
    #         f.writelines(token + '\n')
    #
    # print('token',token)
    # deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'#吴老师模块
    # #deviceId = '7261349d-482e-4454-bc0a-452bb2d533ee'#颜华模块
    # serviceId = r'ZmSer'
    # method = r'CMD'
    # cmdValue = r'A00000'
    #
    # #是否是立即下发
    # EXPIRETIME = 0
    #
    # # local.cmdcode = None
    # # local.cmdinf = None
    # cmdcode,cmdinf = iot.CMD(_token=token,
    #         _deviceId=deviceId,
    #         _serviceId=serviceId,
    #         _method=method,
    #         _cmdvalue=cmdValue,
    #         _expireTime=EXPIRETIME,
    #         _callbackUrl=None)
    # # print('开始介入线程')
    # # threading.Thread(target=threadCMD(
    # #             _token=token,
    # #             _deviceId=deviceId,
    # #             _serviceId=serviceId,
    # #             _method=method,
    # #             _cmdvalue=cmdValue,
    # #             _expireTime=EXPIRETIME,
    # #             _callbackUrl=None,
    # #             _appid=appid,
    # #             _secret=secret,
    # #             _cert=ca
    # #
    # # )).start()
    # # cmdcode, cmdinf = local.cmdcode,local.cmdinf
    # iot = None

    # cmdcode = None
    # cmdinf = None
    # cmdcode = local.cmdinf
    # cmdinf = local.cmdcode
    # threading.Thread(target=distribute(request=request)).start()
    # # return HttpResponse(cmdcode,cmdinf)
    # return HttpResonse('finish')

    # threading.Thread(target=distribute(request)).start()
    
    # bodyStr = json.loads(request.body.decode('utf-8'))
    # threading.Thread(target=distribute,args=(bodyStr)).start()
    # print(request.body.decode('utf-8'))
    # print(bodyStr)

    t = threading.Thread(target=distribute,args=(request,))
    t.start()
    # t.join(timeout=20)
    pass

    if local.cmdcode == None:
        local.cmdcode = 100
    return HttpResponse(local.cmdcode)
    # return HttpResponse('yh')


# 可用 供调试
def test2(request):
    try:
        # bodyStr = json.loads(request.body.decode('utf-8'))
        # print(bodyStr)
        # protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
        # print('\033[31m %s' % (protocol))
        # print('*********************')

        print(f'开始分配线程,--线程名:[{threading.currentThread().getName()}],--线程总数:{threading.activeCount()-1}')

        print(request.body.decode('utf-8'))
        # return None
        bodyStr = json.loads(request.body.decode('utf-8'))
        print(str(bodyStr))

        protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
        print('\033[31m %s' % (protocol))
        print('************************************%s********************************' % (protocol))
        if protocol != 'NF0000442':
            # return HttpResponse('ERR0')
            print('DATA REPORTING')
            return None
        ca = (
            os.path.join(settings.CA_ROOT, r'server.crt'),
            os.path.join(settings.CA_ROOT, r'server.key'),
        )
        token = cache.get('token')

        appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
        secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
        iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)  # 必须要放if外面，否则会报错
        if token == None:
            token = iot.getToken()
            print('reward Token success')
            cache.set('token', token, 60 * 59)
            filePath = os.path.join(settings.CA_ROOT, r'token_his.extend')
            with open(filePath, 'a+') as f:
                f.writelines(token + '\n')

        print('token', token)
        deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'  # 吴老师模块
        # deviceId = '7261349d-482e-4454-bc0a-452bb2d533ee'#颜华模块
        serviceId = r'ZmSer'
        method = r'CMD'
        cmdValue = r'A00000'
        # 是否是立即下发
        EXPIRETIME = 0
        print('开始下发命令，命令有效时间是-->>  %d   (s)' % (EXPIRETIME))
        # local.cmdcode = None
        # local.cmdinf = None
        cmdcode, cmdinf = iot.CMD(_token=token,
                                  _deviceId=deviceId,
                                  _serviceId=serviceId,
                                  _method=method,
                                  _cmdvalue=cmdValue,
                                  _expireTime=EXPIRETIME,
                                  _callbackUrl=None)
        local.cmdcode, local.cmdinf = cmdcode, cmdinf
        print(local.cmdcode, local.cmdinf)

        iot = None
        print('******************************** c a   ^^^^^^^^^^^^^^^^^^^^^^^^^')
    except Exception as ex:
        print(ex)
    return None

def test(request):
    # try:
    print(request.body)
# def threadCMD(_token,
#             _deviceId,
#             _serviceId,
#             _method,
#             _cmdvalue,
#             _expireTime,
#             _callbackUrl,
#               _appid,
#               _secret,
#               _cert,
#               ):
#
#     local.cmdcode,local.cmdinf= iotut.IoT(_appid=_appid, _secret=_secret, _cert=_cert).CMD(
#             _token=_token,
#             _deviceId=_deviceId,
#             _serviceId=_serviceId,
#             _method=_method,
#             _cmdvalue=_cmdvalue,
#             _expireTime=_expireTime,
#             _callbackUrl=_callbackUrl)
#     pass
def distribute(request):
    try:
        # bodyStr = json.loads(request.body.decode('utf-8'))
        # print(bodyStr)
        # protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
        # print('\033[31m %s' % (protocol))
        # print('*********************')

        print(f'开始分配线程,--线程名:[{threading.currentThread().getName()}],--线程总数:{threading.activeCount()-1}')

        # print(request.body.decode('utf-8'))
        # return None
        bodyStr = json.loads(request.body.decode('utf-8'))
        # print(str(bodyStr))

        protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
        # print('\033[31m %s' % (protocol))
        print('************************************%s********************************' % (protocol))
        if protocol != 'NF0000442':
            # return HttpResponse('ERR0')
            print('DATA REPORTING')
            return None
        ca = (
            os.path.join(settings.CA_ROOT, r'server.crt'),
            os.path.join(settings.CA_ROOT, r'server.key'),
        )
        token = cache.get('token')

        appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
        secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
        iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)  # 必须要放if外面，否则会报错
        if token == None:
            token = iot.getToken()
            print('reward Token success')
            cache.set('token', token, 60 * 59)
            filePath = os.path.join(settings.CA_ROOT, r'token_his.extend')
            with open(filePath, 'a+') as f:
                f.writelines(token + '\n')

        print('token', token)
        deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'  # 吴老师模块
        # deviceId = '7261349d-482e-4454-bc0a-452bb2d533ee'#颜华模块
        serviceId = r'ZmSer'
        method = r'CMD'
        cmdValue = r'A00000'
        # 是否是立即下发
        EXPIRETIME = 0
        print('开始下发命令，命令有效时间是-->>  %d   (s)' % (EXPIRETIME))
        # local.cmdcode = None
        # local.cmdinf = None
        cmdcode, cmdinf = iot.CMD(_token=token,
                                  _deviceId=deviceId,
                                  _serviceId=serviceId,
                                  _method=method,
                                  _cmdvalue=cmdValue,
                                  _expireTime=EXPIRETIME,
                                  _callbackUrl=None)
        local.cmdcode, local.cmdinf = cmdcode, cmdinf
        print(local.cmdcode, local.cmdinf)

        iot = None
        print('*---------------------------- e n d -----------------------------*')
    except Exception as ex:
        print(ex)
    return None


# 可用  作废
def distribute1(request):
    try:
        print('开始分配线程')

        print(request.body.decode('utf-8'))
        return None
        bodyStr = json.loads(request.body.decode('utf-8'))
        print(str(bodyStr))

        protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
        print('\033[31m %s'%(protocol))
        print('************************************%s********************************'%(protocol))
        # return HttpResponse(protocol)
        if protocol != 'NF0000442':
            # return HttpResponse('ERR0')
            print('DATA REPORTING')
            return None
        ca = (
            os.path.join(settings.CA_ROOT, r'server.crt'),
            os.path.join(settings.CA_ROOT, r'server.key'),
        )
        token = cache.get('token')

        appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
        secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
        iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)  # 必须要放if外面，否则会报错

        if token == None:
            token = iot.getToken()
            print('reward Token success')
            cache.set('token', token, 60 * 59)
            filePath = os.path.join(settings.CA_ROOT, r'token_his.extend')
            with open(filePath, 'a+') as f:
                f.writelines(token + '\n')

        print('token', token)
        deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'  # 吴老师模块
         # deviceId = '7261349d-482e-4454-bc0a-452bb2d533ee'#颜华模块
        serviceId = r'ZmSer'
        method = r'CMD'
        cmdValue = r'A00000'

        # 是否是立即下发
        EXPIRETIME = 0
        print('开始下发命令，命令有效时间是-->>  %d   (s)'%(EXPIRETIME))
        # local.cmdcode = None
        # local.cmdinf = None
        cmdcode, cmdinf = iot.CMD(_token=token,
                                  _deviceId=deviceId,
                                  _serviceId=serviceId,
                                  _method=method,
                                  _cmdvalue=cmdValue,
                                  _expireTime=EXPIRETIME,
                                  _callbackUrl=None)
        local.cmdcode, local.cmdinf = cmdcode,cmdinf
        print(local.cmdcode, local.cmdinf)

        iot = None
    except Exception as ex:
        print('分配线程后下发命令异常: ',ex)
    # local.cmdcode, local.cmdinf = cmdcode, cmdinf

