import json
import requests

url = "https://dapi.kakao.com/v2/search/web"
queryString = {"query":"류현진"}
headers = {"Authorization": "KakaoAK 5901d17878edcecb95c2b269f289238c"}
response = requests.get(url, headers=headers, params=queryString)
print(json.loads(response.text))