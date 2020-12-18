import os
import json
import requests

def sendToMeMessage(text):
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

text = "카카오 메시지 전송 테스트 중입니다("+os.path.basename(__file__).replace(".py", ")")

KAKAO_TOKEN = "XHByW5dG3fxWGujawVxIXcpmMgsdvDON01F5yAo9c04AAAF2dEggHw"

print(sendToMeMessage(text).text)
