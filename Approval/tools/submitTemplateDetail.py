import requests
from WeChatProject import settings
from Approval.tools import getAccessToken
import json


def submit(subdata, UserId, templateId):
    print("submit "+ subdata)
    requestURL = "https://qyapi.weixin.qq.com/cgi-bin/oa/applyevent?access_token=ACCESS_TOKEN".replace("ACCESS_TOKEN", getAccessToken.getToken())
    data = {
        "creator_userid": UserId,
        "template_id": templateId,
        "use_template_approver": 0,
        "approver": [
            {
                "attr": 1,
                "userid": ["821316134975"]
            }
        ],
        "notifyer": ["821316158175","821316147075"],
        "notify_type": 1,
        #"apply_data": subdata
    }

    data["apply_data"] = json.loads(subdata)

    print(data)
    ResData = requests.post(requestURL, data=json.dumps(data))
    print("*"*30)
    print("ykyk")
    print("*"*30)

    print(ResData.json())
    return ResData.json()