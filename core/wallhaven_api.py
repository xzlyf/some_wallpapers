"""
Api地址：https://wallhaven.cc/help/api
"""
import json
import time

import requests
from requests.adapters import HTTPAdapter

__api_search = "https://wallhaven.cc/api/v1/search"


# 指定数量随机下载  1组大概24张图
def get_random(total):
    page = 1

    # 配置请求超时
    request = requests.Session()
    request.mount('http://', HTTPAdapter(max_retries=5))
    request.mount('https://', HTTPAdapter(max_retries=5))

    while page <= total:
        params = {"sorting": "random", "page": page}
        response = request.get(__api_search, params=params)
        data = json.loads(response.text)
        for pic in data.get("data"):
            _download(pic)
        page += 1
        time.sleep(1)


def _download(pic):
    image = requests.get(pic.get("path"))
    if image.status_code == 200:
        with open("./save/" + pic.get("id", str(round(time.time() * 1000))) + ".jpg", mode="wb")as file:
            file.write(image.content)
            print("缓存成功：" + pic.get("path"))
    else:
        print("缓存失败：" + pic.get("path"))
