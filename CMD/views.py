from django.shortcuts import render
from django.conf import settings
from django.shortcuts import HttpResponse
# Create your views here.
import os
import yh.hy.IoTUtility.IoT as iot
def cmd(request):

    bodyStr = request.body.decode('utf-8')

    filePath = os.path.join(settings.CA_ROOT,r'1.ext')
    with open(filePath,'a+') as f:
        f.writelines(bodyStr + '\n')
    return HttpResponse('ok')