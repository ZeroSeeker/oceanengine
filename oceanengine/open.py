#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests


def get_token(
        app_id: int,
        secret: str,
        auth_code: str
):
    """
    获取token

    :param

    成功返回：
        {
            'message': 'OK',
            'code': 0,
            'data': {
                'advertiser_id': 166************9432,
                'advertiser_name': '中*********4',
                'access_token': '8828********************349135',
                'refresh_token_expires_in': 2591999,
                'advertiser_ids': [
                    16*************2,
                    16*************3
                ],
                'expires_in': 86399,
                'refresh_token': '4c4******************c5'
            },
            'request_id': '202*****************E81'
        }
    失败返回：
        {
            'message': 'auth_code已过期，请重新授权',
            'code': 40110,
            'data': {},
            'request_id': '202206****************139788'
        }
    """
    url = "https://ad.oceanengine.com/open_api/oauth2/access_token/"
    data = {
        "app_id": app_id,
        "secret": secret,
        "grant_type": "auth_code",
        "auth_code": auth_code
    }
    response = requests.post(url=url, json=data)
    return response.json()


def get_refresh_token(
        app_id: int,
        secret: str,
        refresh_token: str
):
    """
    刷新token

    :param

    成功返回：
        {
            'message': 'OK',
            'code': 0,
            'data': {
                'access_token': '765c********************ff',
                'refresh_token_expires_in': 2591999,
                'expires_in': 86399,
                'refresh_token': '868********************173'
            },
            'request_id': '2022*******************30E645'
        }
    失败返回：

    """
    url = "https://ad.oceanengine.com/open_api/oauth2/refresh_token/"
    data = {
        "app_id": app_id,
        "secret": secret,
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    response = requests.post(url=url, json=data)
    return response.json()
