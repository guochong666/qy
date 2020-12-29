from django.urls import path
from . import views

app_name = 'Approval'
urlpatterns = [
    # 获取审批模板
    path('getTemplate/',views.getTemplate),

    # 提交模板
    path('submitTemplate/',views.submitTemplate),

    # 获取企业微信用户id
    path('getUserId/', views.getUserId),

    # 显示所有模板
    path('showTemplateID/',views.showTemplateID),
    path('show/<templateId>',views.approvalTest, name="show"),
]
