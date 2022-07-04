#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests
import json


def get_token(
        app_id: int,
        secret: str,
        auth_code: str
):
    """
    Token管理-获取Access Token

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
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        return_json=True
    )


def get_refresh_token(
        app_id: int,
        secret: str,
        refresh_token: str
):
    """
    Token管理-刷新Refresh Token

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
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        return_json=True
    )


def get_user_info(
        access_token: str,
        debug_mode: int = None
):
    """
    Token管理-获取授权User信息
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710507039756
    :param access_token: 授权access_token，可以通过获取Access token接口获取
    :param debug_mode: 允许值：1（开启）；Debugger模式仅适用于接口测试使用（不适合线上生产环境），目前频控限制为20次/分钟，建议在遇到调用接口报错后，在header中传入此段，以获取错误help message。

    成功返回：
        {
            'code': 0,
            'message': 'OK',
            'request_id': '202**************B63A',
            'data': {
                'display_name': '用户************966',
                'email': 'm***1@163.com',
                'id': 24****************37
            }
        }
    失败返回：
        {
            'code': 40104,
            'message': 'The access_token is empty.',
            'request_id': '20220****************D94E'
        }
    """
    url = "https://ad.oceanengine.com/open_api/2/user/info/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        return_json=True
    )


def get_advertiser(
        access_token: str,
        app_id: int,
        secret: str
):
    """
    Token管理-获取已授权账户
    已授权账户都是大账户，下面有很多子账户
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710506574848
    account_role对照：https://open.oceanengine.com/labels/7/docs/1696710760171535

    CUSTOMER_OPERATOR：账户角色-协作者授权的纵横组织，对应账户管理文档见：https://open.oceanengine.com/labels/7/docs/1696710519122956

    :param access_token: 授权access_token，可以通过获取Access token接口获取
    :param app_id: 开发者申请的应用APP_ID，可通过“应用管理”界面查看
    :param secret: 开发者应用的私钥Secret，可通过“应用管理”界面查看（确保填入secret与app_id对应以免报错！）

    成功返回：
        {
            'code': 0,
            'message': 'OK',
            'request_id': '2022******************C932',
            'data': {
                'list': [
                    {
                        'account_role': 'CUSTOMER_OPERATOR',
                        'advertiser_id': 169**********64,
                        'advertiser_name': '乐******1',
                        'advertiser_role': 2,
                        'company_list': [],
                        'is_valid': True
                    },
                    {
                        'account_role': 'CUSTOMER_OPERATOR',
                        'advertiser_id': 17***********247,
                        'advertiser_name': 'HN******1',
                        'advertiser_role': 2,
                        'company_list': [],
                        'is_valid': True
                    }
                ]
            }
        }
    失败返回：

    """
    url = "https://ad.oceanengine.com/open_api/oauth2/advertiser/get/"
    data = {
        "app_id": app_id,
        "secret": secret,
        "access_token": access_token
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        json=data,
        return_json=True
    )


def get_app_access_token(
        app_id: int,
        secret: str
):
    """
    Token管理-获取APP Access Token
    应用级token获取
    参考文档：https://open.oceanengine.com/labels/7/docs/1713655428885516

    :param app_id: 开发者申请的应用APP_ID，可通过“应用管理”界面查看
    :param secret: 开发者应用的私钥Secret，可通过“应用管理”界面查看（确保填入secret与app_id对应以免报错！）

    成功返回：
    失败返回：

    """
    url = "https://open.oceanengine.com/open_api/oauth2/app_access_token/"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "app_id": app_id,
        "secret": secret,
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        headers=headers,
        return_json=True
    )


def get_agent_advertiser(
        access_token: str,

        advertiser_id: int,
        page: int = None,
        page_size: int = None,
        cursor: str = None,
        count: int = None,

        debug_mode: str = None
):
    """【不完善】
    账号服务-代理商账号管理-代理商管理账户列表
    获取代理商下的账号列表
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710516003852

    :param app_id: 开发者申请的应用APP_ID，可通过“应用管理”界面查看
    :param secret: 开发者应用的私钥Secret，可通过“应用管理”界面查看（确保填入secret与app_id对应以免报错！）

    成功返回：
    失败返回：
        {
            'message': "Account 2*******7 doesn't exist or the role is wrong",
            'code': 40002,
            'data': {},
            'request_id': '20********************D0'
        }

    """
    url = "https://ad.oceanengine.com/open_api/2/agent/advertiser/select/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode

    params = {
        'advertiser_id': advertiser_id
    }
    if page is not None:
        params['page'] = page
    if page_size is not None:
        params['page_size'] = page_size
    if cursor is not None:
        params['cursor'] = cursor
    if count is not None:
        params['count'] = count

    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def get_advertiser_info(
        access_token: str,

        advertiser_ids: list=None,
        fields: list = None,

        debug_mode: str = None
):
    """【不完善】
    账号服务-广告主信息与资质管理-广告主信息
    获取代理商下的账号列表
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710508983311

    :param app_id: 开发者申请的应用APP_ID，可通过“应用管理”界面查看
    :param secret: 开发者应用的私钥Secret，可通过“应用管理”界面查看（确保填入secret与app_id对应以免报错！）

    成功返回：
    失败返回：
        {
            'code': 40002,
            'message': 'advertiserdoesnograntyou/advertiser/info/permission',
            'request_id': '20**************F2A'
        }

    """
    url = "https://ad.oceanengine.com/open_api/2/advertiser/info/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode

    if advertiser_ids is None:
        advertiser_ids = [0]
    if fields is None:
        fields = ["id", "name", "role", "status", "address", "reason", "license_url", "license_no", "license_province", "license_city", "company", "brand", "promotion_area", "promotion_center_province", "promotion_center_city", "industry", "create_time"]
    params = {
        'advertiser_ids': advertiser_ids,
        'fields': fields
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def get_report_agent_v2(
        access_token: str,

        agent_id: int,
        start_date: str,
        end_date: str,

        debug_mode: str = None
):
    """【不完善】
    数据报表-广告数据报表-广告主数据
    获取代理商下的账号列表
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710550620160

    :param app_id: 开发者申请的应用APP_ID，可通过“应用管理”界面查看
    :param secret: 开发者应用的私钥Secret，可通过“应用管理”界面查看（确保填入secret与app_id对应以免报错！）

    成功返回：
    失败返回：
        {
            'code': 40002,
            'message': 'advertiserdoesnograntyou/advertiser/info/permission',
            'request_id': '20**************F2A'
        }

    """
    url = "https://ad.oceanengine.com/open_api/2/report/agent/get_v2/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode
    params = {
        'agent_id': agent_id,
        'start_date': start_date,
        'end_date': end_date
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def get_customer_center_advertiser_list(
        access_token: str,

        cc_account_id: int,
        account_source: str = None,
        page: int = None,
        page_size: int = None,

        debug_mode: str = None
):
    """
    账号服务-纵横组织账户管理-获取纵横组织下资产账户列表（分页）
    获取当前纵横组织下的资产账户列表（广告主，企业号），如果纵横组织下还有子级组织账号，会把cc_account_id下所有可操作的资产账户全量返回
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710520884224

    :param access_token: 授权access_token，可以通过【获取Access token】接口获取
    :param cc_account_id: 纵横组织id，通过【获取已授权账户】接口获取
    :param account_source: 账户类型，可选值：AD 广告主账号、ENTERPRISE企业号，默认值：AD
    :param page: 页码 默认值: 1
    :param page_size: 页面大小 默认值: 10，最大值：100
    :param debug_mode: 允许值：1（开启）；Debugger模式仅适用于接口测试使用（不适合线上生产环境），目前频控限制为20次/分钟，建议在遇到调用接口报错后，在header中传入此段，以获取错误help message。

    成功返回：
        {
            'message': 'OK',
            'code': 0,
            'data': {
                'page_info': {
                    'total_number': 1,
                    'page': 1,
                    'page_size': 10,
                    'total_page': 1
                },
                'list': [
                    {
                        'advertiser_id': 16***********640,
                        'advertiser_type': 'NORMAL',
                        'advertiser_name': '乐***********M'
                    }
                ]
            },
            'request_id': '20220*************6EA'
        }
    失败返回：

    """
    url = "https://ad.oceanengine.com/open_api/2/customer_center/advertiser/list/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode
    params = {
        'cc_account_id': cc_account_id
    }
    if account_source is not None:
        params['account_source'] = account_source
    if page is not None:
        params['page'] = page
    if page_size is not None:
        params['page_size'] = page_size
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def get_report_advertiser(
        access_token: str,

        advertiser_id: int,
        start_date: str,
        end_date: str,
        fields: str = None,
        group_by: str = None,
        time_granularity: str = None,
        filtering: json = None,
        page: int = None,
        page_size: int = None,

        debug_mode: str = None
):
    """
    数据报表-广告数据报表-广告主数据
    此接口用于获取广告账户维度的投放数据，包括消耗、点击、展示等指标，具体可以参考应答参数指标说明。
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710550620160

    :param access_token: 授权access-token，获取方法见接口文档【获取Access-Token】

    :param advertiser_id: 广告主ID
    :param start_date: 起始日期,格式YYYY-MM-DD,只支持查询2016-10-26及以后的日期
    :param end_date: 结束日期,格式YYYY-MM-DD,只支持查询2016-10-26及以后的日期，时间跨度不能超过30天
    :param fields: 指定需要的指标名称，可参考应答参数返回的消耗指标字段 默认值：cost、show、avg_show_cost、click、ctr、avg_click_cost、convert、convert_rate、convert_cost
    :param group_by: 分组条件 默认为STAT_GROUP_BY_FIELD_STAT_TIME，支持多种分组条件，具体详见【分组组合规则】
    :param time_granularity: 时间粒度 默认值: STAT_TIME_GRANULARITY_DAILY 允许值:STAT_TIME_GRANULARITY_DAILY (按天维度),STAT_TIME_GRANULARITY_HOURLY (按小时维度)
    :param filtering: 过滤字段，json格式，支持字段如下
    :param page: 页码 默认值: 1
    :param page_size: 页面大小，即每页展示的数据量 默认值: 20 取值范围: 1-1000

    :param debug_mode: 允许值：1（开启）；Debugger模式仅适用于接口测试使用（不适合线上生产环境），目前频控限制为20次/分钟，建议在遇到调用接口报错后，在header中传入此段，以获取错误help message。

    成功返回：
        {
            'code': 0,
            'message': 'OK',
            'request_id': '2022***************A490',
            'data': {
                'page_info': {
                    'total_page': 1,
                    'page_size': 20,
                    'total_number': 2,
                    'page': 1
                },
                'list': [
                    {
                        'convert': 0,
                        'click': 0,
                        'advertiser_id': 17***********2,
                        'avg_show_cost': 0.0,
                        'convert_cost': 0.0,
                        'avg_click_cost': 0.0,
                        'cost': 0.0,
                        'ctr': 0.0,
                        'stat_datetime': '2022-06-01 00:00:00',
                        'show': 0,
                        'convert_rate': 0.0
                    },
                    {
                        'convert': 0,
                        'click': 0,
                        'advertiser_id': 173*************072,
                        'avg_show_cost': 0.0,
                        'convert_cost': 0.0,
                        'avg_click_cost': 0.0,
                        'cost': 0.0,
                        'ctr': 0.0,
                        'stat_datetime': '2022-06-02 00:00:00',
                        'show': 0,
                        'convert_rate': 0.0
                    }
                ]
            }
        }
    失败返回：


    """
    url = "https://ad.oceanengine.com/open_api/2/report/advertiser/get/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode
    params = {
        'advertiser_id': advertiser_id,
        'start_date': start_date,
        'end_date': end_date
    }
    if fields is not None:
        params['fields'] = fields
    if group_by is not None:
        params['group_by'] = group_by
    if time_granularity is not None:
        params['time_granularity'] = time_granularity
    if filtering is not None:
        params['filtering'] = filtering
    if page is not None:
        params['page'] = page
    if page_size is not None:
        params['page_size'] = page_size
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )


def get_report_ad(
        access_token: str,

        advertiser_id: int,
        start_date: str,
        end_date: str,
        fields: str = None,
        group_by: str = None,
        time_granularity: str = None,
        filtering: json = None,
        order_field: str = None,
        order_type: str = None,

        page: int = None,
        page_size: int = None,

        debug_mode: str = None
):
    """
    数据报表-广告数据报表-广告计划数据
    此接口用于获取广告计划纬度的投放数据，包括消耗、点击、展示等指标，具体可以参考应答参数指标说明
    参考文档：https://open.oceanengine.com/labels/7/docs/1696710551666703

    :param access_token: 授权access-token，获取方法见接口文档【获取Access-Token】

    :param advertiser_id: 广告主ID
    :param start_date: 起始日期,格式YYYY-MM-DD,只支持查询2016-10-26及以后的日期
    :param end_date: 结束日期,格式YYYY-MM-DD,只支持查询2016-10-26及以后的日期，时间跨度不能超过30天
    :param fields: 指定需要的指标名称，可参考应答参数返回的消耗指标字段 默认值：cost、show、avg_show_cost、click、ctr、avg_click_cost、convert、convert_rate、convert_cost
    :param group_by: 分组条件 默认为STAT_GROUP_BY_FIELD_STAT_TIME，支持多种分组条件，具体详见【分组组合规则】
    :param time_granularity: 时间粒度 默认值: STAT_TIME_GRANULARITY_DAILY 允许值:STAT_TIME_GRANULARITY_DAILY (按天维度),STAT_TIME_GRANULARITY_HOURLY (按小时维度)
    :param filtering: 过滤字段，json格式，支持字段如下
    :param order_field: 排序字段，所有的统计指标均可参与排序
    :param order_type: 排序方式；默认值: DESC；允许值: ASC, DESC

    :param page: 页码 默认值: 1
    :param page_size: 页面大小，即每页展示的数据量 默认值: 20 取值范围: 1-1000

    :param debug_mode: 允许值：1（开启）；Debugger模式仅适用于接口测试使用（不适合线上生产环境），目前频控限制为20次/分钟，建议在遇到调用接口报错后，在header中传入此段，以获取错误help message。

    数据更新频率
        数据5～10分钟更新一次
        一般历史数据都不会变，除了数据有问题有校对的情况会更新历史数据，第二天10点可以获取前一天稳定的消耗数据

    成功返回：

    失败返回：


    """
    url = "https://ad.oceanengine.com/open_api/2/report/ad/get/"
    headers = {
        'Access-Token': access_token
    }
    if debug_mode is None:
        pass
    else:
        headers['X-Debug-Mode '] = debug_mode
    params = {
        'advertiser_id': advertiser_id,
        'start_date': start_date,
        'end_date': end_date
    }
    if fields is not None:
        params['fields'] = fields
    if group_by is not None:
        params['group_by'] = group_by
    if time_granularity is not None:
        params['time_granularity'] = time_granularity
    if filtering is not None:
        params['filtering'] = filtering
    if page is not None:
        params['page'] = page
    if page_size is not None:
        params['page_size'] = page_size
    if order_field is not None:
        params['order_field'] = order_field
    if order_type is not None:
        params['order_type'] = order_type
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        params=params,
        return_json=True
    )
