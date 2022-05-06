#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import json


def e_fund_report(
        cookie,
        csrf_token,
        aadvid,
        start_time: int,
        end_time: int,
        limit: int = 10,
        offset: int = 0,  # 后移位数
        time_out: int = 5,
):
    """
    模块功能：采集【财务-资金管理-财务流水】的数据
    精确到子账户
    分页：10/20/30/40 条/页

    :param cookie
    :param csrf_token
    :param aadvid
    :param start_time: 开始时间的时间戳，精确到秒
    :param end_time: 结束时间的时间戳，精确到秒
    :param limit
    :param offset: 偏移量
    :param time_out: 超时时间，单位为秒

    """
    url = "https://e.oceanengine.com/fund_report/api/central/expanditure?appKey=0"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh",
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'content-type': 'application/json;charset=UTF-8',
        "Cookie": cookie,
        'Host': 'e.oceanengine.com',
        "origin": "https://e.oceanengine.com",
        'Pragma': 'no-cache',
        "Referer": f"https://e.oceanengine.com/fund_report/incomeExpanditure?app_key=0&account_id={aadvid}&embed=1&auth_token={csrf_token}&aadvid={aadvid}",
        'TE': 'Trailers',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }
    data = {
        'advertiser_ids': [aadvid],
        'end_time': end_time,  # 结束日期 timestamp
        'limit': limit,  # 每页多少条数据：10/20/30/40
        'offset': offset,  # 后移位数
        'start_time': start_time,  # 开始日期 timestamp
    }
    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        data=json.dumps(data),
        allow_redirects=False,
        timeout=time_out
    )
    return response.json()


def e_fund_report_all(
        cookie,
        aadvid,
        csrf_token,
        start_time: int,
        end_time: int,
        limit: int = 10,
        time_out: int = 5
):
    """
    一次获取全部数据

    :param cookie
    :param csrf_token
    :param aadvid
    :param start_time: 开始时间的时间戳，精确到秒
    :param end_time: 结束时间的时间戳，精确到秒
    :param limit
    :param time_out: 超时时间，单位为秒

    """
    offset = 0
    res_all = list()
    while True:
        res_temp = e_fund_report(
            cookie=cookie,
            aadvid=aadvid,
            csrf_token=csrf_token,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            offset=offset,
            time_out=time_out
        )
        if res_temp is None:
            return
        else:
            code = res_temp.e_fund_report('code')
            if code == 0:
                data = res_temp.e_fund_report('data')
                total_count = data.e_fund_report('total_count')
                advertiser_account = data.e_fund_report('advertiser_account')
                res_all.extend(advertiser_account)
                if len(res_all) >= total_count:
                    return res_all
                else:
                    offset = len(res_all)
            else:
                return
