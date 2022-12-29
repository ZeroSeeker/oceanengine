#!/usr/bin/env python3
# coding = utf8
# 巨量创意相关
import requests


def creative_radar_api__v1__video__info(
        vid: str,
        mid: str
):
    """
    巨量创意-创量灵感 解析创意视频地址
    :param vid: 例如 v02***************tuk0
    :param mid: 例如 7100000000003973
    """
    url = 'https://cc.oceanengine.com/creative_radar_api/v1/video/info'
    data = {
        "video_infos": [
            {
                "vid": vid,
                "mid": mid
            }
        ],
        "water_mark": ""
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "cc.oceanengine.com",
        "Origin": "https://cc.oceanengine.com",
        "Referer": "https://cc.oceanengine.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
        "caller": "cc"
    }
    response = requests.request(
        method='POST',
        url=url,
        json=data,
        headers=headers
    )
    return response.json()
