#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker

此模块为巨量广告的回传功能封装，当前使用最多的是callback_get
"""
from lazysdk import lazyrequests
from urllib import parse
import requests
import time


def callback_get(
        callback: str,
        event_type: int = 0
):
    """
    默认最简单的回传，使用callback和event_type直接拼接回传
    一般回传激活和付费
    :param callback: 点击检测下发的 callback
    :param event_type: 代表的是事件类型，详情见：https://open.oceanengine.com/labels/7/docs/1696710656359439，摘抄部分如下：
        取值	事件名称	定义
        0 激活 用户下载安装完毕应用之后，在联网环境下打开应用
        1 注册 完成应用下载并且在联网环境打开应用后，完成个人账号/游戏角色注册信息提交
        2 付费 完成应用下载并且在联网环境打开应用后，应用内完成一笔付款
        3 表单 完成表单填写并提交
        4 在线咨询 用户点击在线咨询按钮
        5 有效咨询 用户在消息咨询页面内完成至少一句消息对话
        6 次留 用户激活后次日联网环境下打开应用
        20 app内下单 在应用内完成一次订单提交，例如：点击“立即下单”
        21 app内访问 用户成功打开访问应用
        22 app内添加购物车 在应用内成功将商品加入购物车，例如：点击“加入购物车”
        23 app内付费 在应用内完成一次订单付费。目前主要是电商行业使用，常规建议使用付费事件
        25 关键行为 用户在应用内发生的关键行为/行为集合，若是关键行为集合一般是有关联的行为路径。（举例：某直播类客户以注册+发送弹幕作为关键行为转化目标，电商用注册+收藏商品+加入购物车+下单等）
    标准返回：
    {
        "code": 0,
        "ret": 0,
        "msg": "success",
    }
    最主要的两个字段是 code 和 msg，code 等于 0 表示请求正常
    失败示例:code 不为 0。msg 会返回错误的提示信息。
    常见错误:
        错误信息	含义
        missing params callback | callback_param / callback_url / link 字段没有传入
        params muid is empty | 设备信息没有填写或填写错误
    """
    callback = parse.unquote(callback)
    return lazyrequests.lazy_requests(
        method='GET',
        url=callback,
        params={'event_type': event_type},
        return_json=True
    )


def callback_post(
        callback: str,
        action_type,
        action_value=None
):
    """
    回传功能
    :param callback: 回传参数
    :param action_type: 回传类型
    :param action_value: 回传类型对于金额
    """
    callback = parse.unquote(callback)
    if action_value is None:
        actions = [
                {
                    "action_type": action_type
                }
            ]
    else:
        actions = [
            {
                "action_type": action_type,
                "value": str(action_value)
            }
        ]
    return lazyrequests.lazy_requests(
        method='POST',
        url=callback,
        json={'actions': actions},
        return_json=True
    )


def base_send_request(
        request_params: dict,  # 全部参数的值要转换为数值
        request_url: str = "https://ad.oceanengine.com/track/activate/"  # 上报数据的接口
):
    """
    回传文档：https://open.oceanengine.com/doc/index.html?key=ad&type=api&id=1696710647473167
    request_url="https://ad.oceanengine.com/track/activate/?link=__LINK__&source=__SOURCE__&conv_time=__CONV_TIME__&event_type=__EVENT_TYPE__"
    request_params={
        "callback": "EJiw267wvf*************NTczNTBIAQ==",
        "imei": "0c2*************e70e",
        "os": "1",
        "event_type": "2",
        "conv_time": str(int(time.time())),
        "link": 'https://www.chengzijianzhan.com/tetris/page/69794**********************vetype=1'
    }
    其中的link必填
    回传参数说明：https://open.oceanengine.com/doc/index.html?key=ad&type=api&id=1696710647473167
        link （必填），拼接了参数的落地页链接
        event_type（必填回传参数）：2 付费
        conv_time：int（整型）建议填写（填写付费时间）
        source：string（字符串）建议填写（不填）

    但是说明文档说的用ip+ua匹配后直接用回调地址回传，文档见：https://bytedance.feishu.cn/docs/doccnOaxIYGeXokJUqHJGhm86Xf
    """
    return lazyrequests.lazy_requests(
        method='GET',
        url=request_url,
        params=request_params,
        return_json=True
    )


def send_request_quick_app_v2(
        callback: str = None
):
    """
    快应用API回传
    文档：https://event-manager.oceanengine.com/docs/8650/quickapp/
    文档2：https://event-manager.oceanengine.com/docs/8650/app_api_docs/
    """
    url = 'https://analytics.oceanengine.com/api/v2/conversion'
    data = {
        "event_type": "active_pay",
        "context": {
            "ad": {
                "callback": callback,
            }
        },
        "timestamp": int(time.time() * 1000)
    }
    response = requests.post(
        url=url,
        json=data
    )
    return response

