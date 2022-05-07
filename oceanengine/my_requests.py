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


def my_requests(
        method,
        url,
        timeout_retry: bool = True,
        **kwargs
):
    """
    timeout_retry: 超时重试，为True会自动重试，否则不会自动重试
    """
    while True:
        if timeout_retry is True:
            try:
                response = requests.request(
                    method=method,
                    url=url,
                    **kwargs
                )
                return response.json()
            except requests.exceptions.ReadTimeout:
                showlog.warning('连接超时，将在1秒后重试...')
                time.sleep(1)
        else:
            return requests.request(
                method=method,
                url=url,
                **kwargs
            )
