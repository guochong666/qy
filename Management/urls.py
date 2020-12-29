from django.urls import path
from . import views

app_name = 'Management'
urlpatterns = [
    # 登录登出
    path('login/',views.login,name="login"),
    path('loginRes/',views.loginRes,name="loginRes"),
    path('logout/',views.logout,name="logout"),

    # 首页
    path('index/',views.index,name="index"),

    # 审批
    path('showApproval/',views.showApproval,name="showApproval"),
    path('addTemplate/',views.addTemplate,name="addTemplate"),
    path('deleteTemplate/<del_ID>',views.deleteTemplate,name="deleteTemplate"),
    path('searchTemplate/',views.searchTemplate,name="searchTemplate"),

    # 信息采集
    path('showInfo/',views.showInfo,name="showInfo"),
]