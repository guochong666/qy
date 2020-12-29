import requests
from WeChatProject import settings
import json
import time


def getToken():
    with open("Approval/tools/saveAccessToken.json", 'r+', encoding='utf8')as sAT:
    #with open('../saveAccessToken.json', 'r+', encoding='utf8')as sAT:
        ATdata = json.loads(sAT.read())
        now = time.time()
        if int(now - ATdata.get('time')) < 7190:
            access_token = ATdata.get('access_token')
        else:
            sAT.truncate(0)
            sAT.seek(0)
            getURL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            data = {'corpid': settings.corpid,
                    'corpsecret': settings.corpsecret
                    }
            ResData = requests.get(getURL, data)
            access_token = json.loads(ResData.text).get('access_token')
            newJson = {
                "access_token": access_token,
                "time": now
            }
            json.dump(newJson, sAT)
    return access_token


if __name__ == "__main__":
    print(getToken())

