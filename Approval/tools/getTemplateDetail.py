import requests
from WeChatProject import settings
from Approval.tools import getAccessToken
import json


def getTemplateDetail(templateId):
    requestURL = "https://qyapi.weixin.qq.com/cgi-bin/oa/gettemplatedetail?access_token=ACCESS_TOKEN".replace("ACCESS_TOKEN", getAccessToken.getToken())
    data = {
        # 'template_id' : "Bs7yoCAcbDvcm9SmMRHDAntkdg4zrPsXu7mqLr9rX"
        'template_id' : templateId
    }
    ResData = requests.post(requestURL, data=json.dumps(data))
    # print(ResData.json())
    return ResData.json()

# if __name__ == "__main__":
#     getTemplateDetail()