from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse
# Create your views here.
import os
import yh.hy.IoTUtility.IoT as iotut
import yh.hy.Const.IoTConst as iotconst
from django.core.cache import cache
import json
def cmd(request):


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
    with open(os.path.join(settings.CA_ROOT,'log.ini'),'a+') as f:
        f.writelines(str( request.body) + '\n')
    return HttpResponse('write ok')
    bodyStr = json.loads( request.body.decode('utf-8') )
    protocol = bodyStr['services'][0]['data']['serviceData']['MeterReading']['datas'][0]['protocol']
    print(protocol)
    return HttpResponse(protocol)
    if protocol != 'NF0000442':
        return HttpResponse('ERR0')
    ca = (
        os.path.join(settings.CA_ROOT,r'server.crt'),
        os.path.join(settings.CA_ROOT, r'server.key'),
    )
    token = cache.get('token')

    appid = r'4Ixi2dFrkeCLDchfpQwRsSYS0ewa'
    secret = r'JvitPmDQuLoncCiQyYzYOsBaIK4a'
    iot = iotut.IoT(_appid=appid, _secret=secret, _cert=ca)


    if token==None:
        token = iot.getToken()
        cache.set('token',token,60*30)
        # filePath = os.path.join(settings.CA_ROOT,r'1.ext')
        # with open(filePath,'a+') as f:
        #     f.writelines(token + '\n')

    print('token',token)
    deviceId = '4720af4a-4d47-42ed-a421-40cc05d24279'
    serviceId = r'ZmSer'
    method = r'CMD'
    cmdValue = r'A00000'
    cmdcode,cmdinf = iot.CMD(_token=token,
            _deviceId=deviceId,
            _serviceId=serviceId,
            _method=method,
            _cmdvalue=cmdValue,
            _expireTime=0,
            _callbackUrl=None)
    return HttpResponse(cmdcode,cmdinf)