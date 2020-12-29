import pymysql
from Approval.models import TemplateId
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Approval.tools import getTemplateDetail,submitTemplateDetail, getAccessToken
import json
import requests

def getTemplate(request):
    print("hhhh")
    # 获取审批模板详情
    templateId = request.session.get('templateId')
    # templateId = "BsAYLu7PXApNSRuL3veJZmSy34eggwsjq8Xa8dLg5"      # 信息学院新闻发布
    # templateId = "Bs7yoCAcbDvcm9SmMRHDAntkdg4zrPsXu7mqLr9rX"        # 审批测试
    temp = {
        'data': getTemplateDetail.getTemplateDetail(templateId)
    }

    print(templateId + "gg")
    # 跨域、乱码
    response = JsonResponse(temp, safe=False, json_dumps_params={'ensure_ascii': False})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def submitTemplate(request):
    # 提交从前端获取的审批数据到企业微信服务器
    print("===")
    print(request.method)
    print(str(request.POST.dict()))
    UserId = request.session.get('UserId')
    templateId = request.session.get('templateId')
    postdata = ""
    for key in request.POST.dict():
        postdata = key
    if request.method == 'POST':
        print(postdata)

        temp = submitTemplateDetail.submit(postdata, UserId, templateId)


        print("1111")
        response = JsonResponse(temp, safe=False, json_dumps_params={'ensure_ascii': False})
        # print(response['errcode'])
        # if response['errcode'] == 0:
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return HttpResponse(response)
        # else:
        #     return HttpResponse()
    else:
        return HttpResponse()

def approvalTest(request, templateId):
    # templateId = "Bs7yoCAcbDvcm9SmMRHDAntkdg4zrPsXu7mqLr9rX"
    # templateId = request.GET.get('templateId')
    templateId = TemplateId.objects.get(ID=templateId).ID
    # print("templateId:",templateId)
    request.session['templateId'] = templateId
    return render(request, "Approval/approvalTest.html")

def showTemplateID(request):
    id_list = TemplateId.objects.all()
    return render(request, 'Approval/showTemplate.html',{'id_list': id_list})

def getUserId(request):
    code = request.GET.get('code')
    requestURL = 'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=ACCESS_TOKEN'.replace("ACCESS_TOKEN", getAccessToken.getToken())
    print("*"*30)
    print(code)
    print(requestURL)
    print("*"*30)
    data = {
            'code': code
    }
    res = requests.get(requestURL, data)
    UserId = json.loads(res.text).get('UserId')


    print(UserId)
    if UserId == None:
        return HttpResponse()
    else:
        request.session['UserId'] = UserId
        return JsonResponse({'UserId':UserId})




