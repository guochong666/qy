from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from Management.models import User
from Approval.models import TemplateId
import json

# 验证登录
def login(request):
    return render(request,"Management/login.html")

def loginRes(request):
    uid = request.POST.get('uid')
    pwd = request.POST.get('pwd')

    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        user = None
    
    if(user):
        if(pwd == user.password):
            request.session['uid'] = uid
            request.session['isLogin'] = True
            return redirect('../index',{'uid':uid})
        else:
            return render(request,'Management/login.html',{'login_msg':'用户名或密码错误!'})
    else:
        return render(request,'Management/login.html',{'login_msg':'用户不存在!'})

def logout(request):
    request.session['isLogin'] = None
    return render(request,'Management/login.html',{'login_msg':''})

# 访问主页
def index(request):
    if request.session.get('isLogin'): 
        return render(request,'Management/index.html',{'uid':request.session.get('uid')})
    else:
        return render(request,'Management/login.html',{'login_msg':''})

# 审批
def showApproval(request):
    id_list = TemplateId.objects.all()      # 获取所有模板数据
    uid = request.session['uid']            # 获取当前用户
    return render(request,'Management/showApproval.html',{'uid':uid,'id_list':id_list})

def addTemplate(request):
    t_name = request.POST.get('t_name')
    t_ID = request.POST.get('t_ID')
    t_message = request.POST.get('t_message')
    # print("t_name:",t_name,"t_ID:",t_ID,"t_message:",t_ID)

    id = TemplateId.objects.filter(ID=t_ID).first()
    if id is None:
        id = TemplateId()
        id.ID = t_ID
        id.name = t_name
        id.message = t_message
        id.save()
        # return redirect(request,'Management/showApproval.html')

    id_list = TemplateId.objects.all()      # 获取所有模板数据
    uid = request.session['uid']            # 获取当前用户
    return render(request,'Management/showApproval.html',{'id_list':id_list,'uid':uid})
 
def deleteTemplate(request,del_ID):
    id = TemplateId.objects.filter(ID=del_ID).delete()  # 删除该记录
    id_list = TemplateId.objects.all()      # 获取所有模板数据
    uid = request.session['uid']            # 获取当前用户
    return render(request,'Management/showApproval.html',{'id_list':id_list,'uid':uid})

def searchTemplate(request):
    search_ID = request.POST.get('search_ID')

    if len(search_ID) == 0:
        search_msg = "请输入要查询的模板ID!"
        id_list = TemplateId.objects.all()      # 获取所有模板数据
    else:
        id_list = TemplateId.objects.filter(ID__contains = search_ID)      
        if id_list.exists():
            search_msg = "查询结果如下"
        else:
            search_msg = "没有该模板!"

    print(id_list,search_msg)
    
    uid = request.session['uid']            # 获取当前用户
    return render(request,'Management/showApproval.html',{'id_list':id_list,'uid':uid,'search_msg':search_msg})


# 信息采集
def showInfo(request):
    uid = request.session['uid']            # 获取当前用户
    return render(request,'Management/showInfo.html',{'uid':uid}) 