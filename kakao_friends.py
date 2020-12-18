import json
import requests

def getFriendsList():
    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 정보 요청

    result = json.loads(requests.get(url, headers=header).text)

    print("result: {}".format(result))

    friends_list = result.get("elements")
    friends_id = []

    print(requests.get(url, headers=header).text)
    print(friends_list)

    for friend in friends_list:
        friends_id.append(str(friend.get("uuid")))

        return friends_id


KAKAO_TOKEN = "1UE1QSyVmF3jgoYGWrlfLSroqmGiRuEEHzKhTgo9dZwAAAF2dNUOGQ"

getFriendsList()
