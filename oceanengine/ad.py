#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests
from lazysdk import lazytime
import datetime


def promote_ad_list(
        aadvid,
        cookie: str,
        csrf_token: str,
        page: int = 1,
        limit: int = 20,
        timeout: int = 5,
        start_time: datetime.date = lazytime.get_relative_date(0),
        end_time: datetime.date = lazytime.get_relative_date(0),
        sort_stat: str = 'create_time',
        sort_order: int = 1,
        fields: list = None
):
    """
    【推广】-【计划】
    返回：
    {
        "code": 0,
        "data": {
            "ads": [
                {...},
                {...}
            ],
            "total_metrics": {...},
            "pagination": {
                "page": 2,
                "page_size": 20,
                "total_page": 5,
                "total_count": 91
            }
        },
        "extra": {

        },
        "msg": "",
        "request_id": "..."
    }
    """
    url = "	https://ad.oceanengine.com/nbs/api/promote/ad/list?aadvid=%s" % aadvid
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        # "Connection": "keep-alive",
        "Content-Type": "application/json; charset=utf-8",
        "Cookie": cookie,
        "Host": "ad.oceanengine.com",
        "Origin": "https://ad.oceanengine.com",
        "Referer": "https://ad.oceanengine.com/pages/promotion.html?aadvid=%s" % aadvid,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        "X-CSRFToken": csrf_token
    }
    if fields is None:
        fields = [  # 列
                "stat_cost",
                "show_cnt",
                "cpm_platform",
                "click_cnt",
                "cpc_platform",
                "ctr",
                "convert_cnt",
                "conversion_cost",
                "conversion_rate",
                "deep_convert_cnt",
                "deep_convert_cost",
                "deep_convert_rate",
                "attribution_convert_cnt",
                "attribution_convert_cost",
                "attribution_conversion_rate",
                "attribution_deep_convert_cnt",
                "attribution_deep_convert_cost",
                "attribution_deep_convert_rate",
                "attribution_event_weight",
                "attribution_event_weight_roi",
                "pre_convert_count",
                "pre_convert_cost",
                "pre_convert_rate",
                "click_start_cnt",
                "click_start_cost",
                "click_start_rate",
                "download_finish_cnt",
                "download_finish_cost",
                "download_finish_rate",
                "install_finish_cnt",
                "install_finish_cost",
                "install_finish_rate",
                "active",
                "active_cost",
                "active_rate",
                "active_register",
                "active_register_cost",
                "active_register_rate",
                "game_addiction",
                "game_addiction_cost",
                "game_addiction_rate",
                "active_pay",
                "active_pay_cost",
                "active_pay_rate",
                "game_pay_count",
                "game_pay_cost",
                "attribution_game_pay_7d_count",
                "attribution_game_pay_7d_cost",
                "attribution_active_pay_7d_per_count",
                "in_app_uv",
                "in_app_detail_uv",
                "in_app_cart",
                "in_app_pay",
                "in_app_order",
                "attribution_next_day_open_cnt",
                "attribution_next_day_open_cost",
                "attribution_next_day_open_rate",
                "next_day_open",
                "attribution_retention_2d_cnt",
                "attribution_retention_2d_cost",
                "attribution_retention_2d_rate",
                "attribution_retention_3d_cnt",
                "attribution_retention_3d_cost",
                "attribution_retention_3d_rate",
                "attribution_retention_4d_cnt",
                "attribution_retention_4d_cost",
                "attribution_retention_4d_rate",
                "attribution_retention_5d_cnt",
                "attribution_retention_5d_cost",
                "attribution_retention_5d_rate",
                "attribution_retention_6d_cnt",
                "attribution_retention_6d_cost",
                "attribution_retention_6d_rate",
                "attribution_retention_7d_cnt",
                "attribution_retention_7d_cost",
                "attribution_retention_7d_rate",
                "attribution_retention_7d_sum_cnt",
                "attribution_retention_7d_total_cost",
                "phone",
                "form",
                "form_submit",
                "map",
                "button",
                "view",
                "download_start",
                "qq",
                "lottery",
                "vote",
                "message",
                "redirect",
                "shopping",
                "consult",
                "consult_effective",
                "phone_confirm",
                "phone_connect",
                "phone_effective",
                "coupon",
                "coupon_single_page",
                "redirect_to_shop",
                "poi_address_click",
                "poi_collect",
                "customer_effective",
                "attribution_customer_effective",
                "attribution_customer_effective_cost",
                "attribution_clue_pay_succeed",
                "attribution_clue_pay_succeed_cost",
                "attribution_clue_interflow",
                "attribution_clue_interflow_cost",
                "attribution_clue_high_intention",
                "attribution_clue_high_intention_cost",
                "attribution_clue_confirm",
                "attribution_clue_confirm_cost",
                "consult_clue",
                "oto_pay_count",
                "oto_stay_count",
                "live_groupon_product_click_count",
                "live_groupon_pay_click_count",
                "live_groupon_pay_order_count",
                "live_groupon_pay_order_stat_cost",
                "dy_follow",
                "message_action",
                "dy_home_visited",
                "click_landing_page",
                "click_shopwindow",
                "click_website",
                "click_download",
                "click_call_dy",
                "click_counsel",
                "click_call_cnt",
                "coupon_addition",
                "form_click_button",
                "shake_count",
                "attach_creative_show_cnt",
                "attach_creative_click_cnt",
                "total_play",
                "play_duration_3s",
                "valid_play",
                "valid_play_cost",
                "valid_play_rate",
                "valid_play_of_mille",
                "valid_play_cost_of_mille",
                "play_25_feed_break",
                "play_50_feed_break",
                "play_75_feed_break",
                "play_99_feed_break",
                "average_play_time_per_play",
                "play_over_rate",
                "wifi_play_rate",
                "card_show",
                "dy_like",
                "dy_comment",
                "dy_share",
                "ad_dislike_cnt",
                "ad_report_cnt",
                "ies_challenge_click",
                "ies_music_click",
                "location_click",
                "luban_live_enter_cnt",
                "live_watch_one_minute_count",
                "luban_live_follow_cnt",
                "live_fans_club_join_cnt",
                "luban_live_comment_cnt",
                "luban_live_share_cnt",
                "luban_live_gift_cnt",
                "luban_live_gift_amount",
                "luban_live_slidecart_click_cnt",
                "luban_live_click_product_cnt",
                "luban_live_pay_order_count",
                "luban_live_pay_order_stat_cost",
                "live_pay_order_cost_per_order",
                "live_component_click_count",
                "live_component_click_cost",
                "live_component_click_rate",
                "fans_home_visited_count",
                "fans_video_play_count",
                "fans_dy_like_count",
                "fans_dy_comment_count",
                "fans_video_share_count",
                "fans_luban_live_enter_count",
                "fans_luban_live_comment_count",
                "fans_luban_live_gift_amount",
                "fans_luban_live_slidecart_click_count",
                "fans_luban_live_submit_order_count",
                "fans_luban_live_pay_order_stat_cost",
                "luban_order_cnt",
                "luban_order_stat_amount",
                "luban_order_roi",
                "attribution_game_in_app_ltv_1day",
                "attribution_game_in_app_ltv_2days",
                "attribution_game_in_app_ltv_3days",
                "attribution_game_in_app_ltv_4days",
                "attribution_game_in_app_ltv_5days",
                "attribution_game_in_app_ltv_6days",
                "attribution_game_in_app_ltv_7days",
                "attribution_game_in_app_ltv_8days",
                "attribution_game_in_app_roi_1day",
                "attribution_game_in_app_roi_2days",
                "attribution_game_in_app_roi_3days",
                "attribution_game_in_app_roi_4days",
                "attribution_game_in_app_roi_5days",
                "attribution_game_in_app_roi_6days",
                "attribution_game_in_app_roi_7days",
                "attribution_game_in_app_roi_8days",
                "attribution_day_acitve_pay_count",
                "attribution_day_acitve_pay_cost",
                "attribution_day_acitve_pay_rate",
                "active_pay_intra_day_count",
                "active_pay_intra_day_cost",
                "active_pay_intra_day_rate",
                "attribution_active_pay_intra_one_day_count",
                "attribution_active_pay_intra_one_day_cost",
                "attribution_active_pay_intra_one_day_rate",
                "attribution_active_pay_intra_one_day_amount",
                "attribution_active_pay_intra_one_day_roi",
                "attribution_active_pay_7d_count",
                "attribution_active_pay_7d_cost",
                "attribution_active_pay_7d_rate",
                "attribution_micro_game_0d_ltv",
                "attribution_micro_game_3d_ltv",
                "attribution_micro_game_7d_ltv",
                "attribution_micro_game_0d_roi",
                "attribution_micro_game_3d_roi",
                "attribution_micro_game_7d_roi",
                "stat_union_ltv_0",
                "stat_union_ltv_3",
                "stat_union_ltv_7",
                "union_roi_0",
                "union_roi_3",
                "union_roi_7",
                "wechat",
                "loan_completion",
                "loan_completion_cost",
                "loan_completion_rate",
                "loan_credit",
                "loan_credit_cost",
                "loan_credit_rate",
                "pre_loan_credit",
                "pre_loan_credit_cost",
                "insurance_lt_roi",
                "loan",
                "loan_cost",
                "loan_rate",
                "premium_payment_count",
                "premium_payment_cost",
                "bankcard_information_count",
                "personal_information_count",
                "certification_information_count",
                "open_account_count",
                "first_class_count",
                "second_class_count",
                "unfollow_in_wechat_count",
                "in_wechat_pay_count",
                "low_loan_credit_count",
                "high_loan_credit_count",
                "withdraw_m2_count",
                "submit_certification_count",
                "approval_count",
                "first_order_count",
                "first_rental_order_count",
                "commute_first_pay_count"
            ]
    data = {
        "purchase_type": [
            0
        ],
        "ad_status": [
            0
        ],
        "page": page,
        "limit": limit,
        "sort_stat": sort_stat,
        "sort_order": sort_order,
        "st": str(start_time),
        "et": str(end_time),
        "interfere": 1,
        "automatic_rule_count": 1,
        "luban_roi_goal": 1,
        "luban_roi_status": 1,
        "native_type": 1,
        "fields": fields,
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        headers=headers,
        json=data,
        timeout=timeout,
        return_json=True
    )


def ad_get_account_and_balance_list(
        cookie: str,
        page: int = 1,
        limit: int = 10,  # limit范围：[1,50]
        timeout: int = 5
):
    url = f"https://ad.oceanengine.com/platform/api/v1/bp/multi_accounts/get_account_and_balance_list/?page={page}&limit={limit}"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }
    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        headers=headers,
        timeout=timeout,
        return_json=True
    )


def ad_overture_discount(
        cookie,
        aadvid,

        timeout: int = 5,
        retry_delay: int = 1,  # 重试延时
        retry_limit: int = -1,  # 重试次数限制，-1为无限制
        return_json: bool = True,  # 是否返回json数据
        ReadTimeout_retry: bool = True,  # 超时重试
        JSONDecodeError_retry: bool = True,  # 返回非json类型重试
        ConnectionError_retry: bool = True,  # 连接错误重试
):
    """
    【财务-活动与赠款-已获赠款】
    精确到子账户
    :param cookie:
    :param aadvid:
    :param timeout: 超时时间，单位为秒
    :param timeout_retry: 超时重试
    :param json_error_retry: 返回json错误重试
    """
    method = 'GET'
    url = f"https://ad.oceanengine.com/overture/discount/api/coupon/?aadvid={aadvid}"
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": cookie,
        "referer": f"https://ad.oceanengine.com/overture/discount/coupon/?aadvid={aadvid}",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    return lazyrequests.lazy_requests(
        method=method,
        url=url,
        headers=headers,

        timeout=timeout,
        retry_delay=retry_delay,
        retry_limit=retry_limit,
        return_json=return_json,
        ReadTimeout_retry=ReadTimeout_retry,
        JSONDecodeError_retry=JSONDecodeError_retry,
        ConnectionError_retry=ConnectionError_retry
    )


def notification_msg_list(
        cookie,
        aadvid,
        page: int = 1,

        timeout=5,
        retry_delay: int = 1,  # 重试延时
        retry_limit: int = -1,  # 重试次数限制，-1为无限制
        return_json: bool = True,  # 是否返回json数据
        ReadTimeout_retry: bool = True,  # 超时重试
        JSONDecodeError_retry: bool = True,  # 返回非json类型重试
        ConnectionError_retry: bool = True,  # 连接错误重试
):
    """
    巨量引擎-消息中心-消息列表 财务消息
    """
    method = 'GET'
    url = f"https://ad.oceanengine.com/platform/api/v1/notification/msg_list/?page={page}&msg_category=0&limit=10&aadvid={aadvid}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": cookie,
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    }
    return lazyrequests.lazy_requests(
        method=method,
        url=url,
        headers=headers,
        timeout=timeout,

        retry_delay=retry_delay,
        retry_limit=retry_limit,
        return_json=return_json,
        ReadTimeout_retry=ReadTimeout_retry,
        JSONDecodeError_retry=JSONDecodeError_retry,
        ConnectionError_retry=ConnectionError_retry
    )
