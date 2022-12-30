#!/usr/bin/env python3
# coding = utf8
# 手机头条香相关
import requests


def info_v2(
        item_id: str
):
    """
    手机头条视频解析 依据item_id(site_id)，解析的结果可获得vid(video_id)，以供进一步解析
    item_id位置：可从url中分析，302后的：https://m.toutiao.com/article/【item_id】/?app=news_article
    vid位置：response['data']['video_id']
    :param item_id: 例如 7100000000003973
    """
    url = f'https://m.toutiao.com/i{item_id}/info/v2/'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Host": "m.toutiao.com",
        "Referer": "https://m.toutiao.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers
    )
    try:
        return response.json()
    except:
        return {'code': -1, 'msg': response.text}
