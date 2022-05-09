#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import showlog
import time


def requests_timeout(
        method,
        url,
        timeout_retry: bool = True,
        **kwargs
):
    """
    timeout_retry: 超时重试，为True会自动重试，否则不会自动重试
    """
    while True:
        try:
            return requests.request(
                method=method,
                url=url,
                **kwargs
            )
        except requests.exceptions.ReadTimeout:
            if timeout_retry is True:
                showlog.warning('连接超时，将在1秒后重试...')
                time.sleep(1)
            else:
                return requests.request(
                    method=method,
                    url=url,
                    **kwargs
                )


def requests_json(
        method,
        url,
        timeout_retry: bool = True,
        json_error_retry: bool = True,
        **kwargs
):
    """
    timeout_retry: 超时重试，为True会自动重试，否则不会自动重试
    """
    while True:
        try:
            return requests.request(
                method=method,
                url=url,
                **kwargs
            ).json()
        except requests.exceptions.ReadTimeout:
            if timeout_retry is True:
                showlog.warning('连接超时，将在1秒后重试...')
                time.sleep(1)
            else:
                return requests.request(
                    method=method,
                    url=url,
                    **kwargs
                ).json()
        except requests.exceptions.JSONDecodeError:
            if json_error_retry is True:
                showlog.warning('返回json格式错误，将在1秒后重试...')
                time.sleep(1)
            else:
                return requests.request(
                    method=method,
                    url=url,
                    **kwargs
                ).json()
