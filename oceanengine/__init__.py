#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
import requests
import time_box
import datetime
"""
code:
    0:正常
    40001:未登录
"""


def business_bm_user_global_var(
        cookie: str,
        csrf_token: str,
        time_out: int = 5
):
    """
    【设置】
    成功返回：
    {
        "code": 0,
        "data": {
            "core_user_email": "...",
            "core_user_mobile": "",
            "core_user": {
                "core_user_email": "...",
                "core_user_mobile": "",
                "id": ...,
                "img": "https://p9-passport.byteacctimg.com/img/....image",
                "name": "...",
                "total_accounts": ...
            },
            "org_info": {

            },
            "tcc_conf": {
                "cdnDomainGroup": {...},
                "ad_fe_water_mark_version": "...",
                "bi_tool_admin": [...]
            },
            "GLOBAL_CONF": "{}",
            "login_type": 0,
            "funcs_opened_user": [...]
        },
        "extra": {

        },
        "msg": "",
        "request_id": "..."
    }

    失败返回：
    {
        'code': 40001,
        'data': {

        },
        'extra': {
            'redirect_url': 'https: //business.oceanengine.com/site/login'
        },
        'msg': '未登录',
        'request_id': '...'
    }
    """
    url = 'https://business.oceanengine.com/nbs/api/bm/user/global_var/'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "business.oceanengine.com",
        "Referer": "https://business.oceanengine.com/site/setting/ies-biz-account",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        "x-csrftoken": csrf_token
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        timeout=time_out
    )
    return response.json()


def business_bm_user_login_status(
        cookie: str,
        csrf_token: str,
        time_out: int = 5
):
    """
    大账号
    检验登录状态
    成功返回：
    {
        'code': 0,
        'data': {
            'CoreUser': {
                'UserId': '...'
            },
            'FushenUser': {
                'Staff': {

                }
            },
            'LoginType': 0,
            'Advertiser': {
                'Id': ''
            }
        },
        'extra': {

        },
        'msg': '',
        'request_id': '...'
    }

    失败返回：
    {
        'code': 40001,
        'data': {

        },
        'extra': {
            'redirect_url': 'https: //business.oceanengine.com/site/login'
        },
        'msg': '未登录',
        'request_id': '...'
    }

    """
    url = 'https://business.oceanengine.com/nbs/api/bm/user/login_status'
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9",
        "cookie": cookie,
        "referer": "https://business.oceanengine.com",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "x-csrftoken": csrf_token
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        timeout=time_out
    )
    return response.json()


def business_bm_user_id(
        cookie: str,
        csrf_token: str,
        time_out: int = 5
):
    """
    直接获取user_id
    """
    bm_user_login_status_res = bm_user_login_status(
        cookie=cookie,
        csrf_token=csrf_token,
        time_out=time_out
    )
    if bm_user_login_status_res['code'] == 0:
        data = bm_user_login_status_res.get('data')
        if data is not None:
            core_user = data.get('CoreUser')
            if core_user is not None:
                user_id = core_user.get('UserId')
                bm_user_login_status_res['user_id'] = user_id
                return bm_user_login_status_res
            else:
                return bm_user_login_status_res
        else:
            return bm_user_login_status_res
    else:
        return bm_user_login_status_res


def ad_get_account_and_balance_list(
        cookie: str,
        page: int = 1,
        limit: int = 10,  # limit范围：[1,50]
        time_out: int = 5
):
    url = "https://ad.oceanengine.com/platform/api/v1/bp/multi_accounts/get_account_and_balance_list/?page=%s&limit=%s" % \
                  (page, limit)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        allow_redirects=False,
        timeout=time_out
    )
    return response.json()


def business_bm_dashboard_accounts_list(
        cookie: str,
        csrf_token: str,
        page: int = 1,
        limit: int = 20,
        time_out: int = 5
):
    """
    大账号
    【首页】-【巨量广告详情】-【账户】-【全部巨量广告账户】
    """
    url = "https://business.oceanengine.com/nbs/api/bm/dashboard/accounts_list/?page=%s&limit=%s&app_key=0&search=" % \
          (page, limit)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "business.oceanengine.com",
        "Referer": "https://business.oceanengine.com/site/dashboard?",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        "X-CSRFToken": csrf_token,
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        allow_redirects=False,
        timeout=time_out
    )
    return response.json()


def business_bp_statistics_promote_ad_stats_list(
        cookie: str,
        csrf_token: str,
        page: int = 1,
        limit: int = 20,
        time_out: int = 5,
        start_time: datetime = time_box.get_relative_datetime(0),
        end_time: datetime = time_box.get_relative_datetime(1),
):
    """
    主账号
    【巨量广告】-【推广】-【计划】
    """
    url = "https://business.oceanengine.com/platform/api/v1/bp/statistics/promote/ad/stats_list/"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": cookie,
        "Host": "business.oceanengine.com",
        "Origin": "https://business.oceanengine.com",
        "Referer": "https://business.oceanengine.com/site/promotion?",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0",
        "X-CSRFToken": csrf_token
    }
    data = {
        "start_time": str(start_time),
        "end_time": str(end_time),
        "page": page,
        "limit": limit,
        "order_type": 1,
        "order_field": "create_time",
        "stats_fields": [
            "stat_cost",
            "show_cnt",
            "click_cnt",
            "ctr",
            "cpc_platform",
            "cpm_platform",
            "convert_cnt",
            "conversion_cost",
            "conversion_rate",
            "deep_convert_cnt",
            "deep_convert_cost",
            "deep_convert_rate",
            "stat_grant_cost",
            "stat_cash_cost",
            "attribution_convert_cnt",
            "attribution_convert_cost",
            "attribution_deep_convert_cnt",
            "attribution_deep_convert_cost",
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
            "attribution_next_day_open_cnt",
            "attribution_next_day_open_cost",
            "attribution_next_day_open_rate",
            "next_day_open",
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
            "dy_follow",
            "message_action",
            "dy_home_visited",
            "click_landing_page",
            "click_shopwindow",
            "click_website",
            "click_download",
            "click_call_dy",
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
            "luban_live_pay_order_count_by_author_3days",
            "luban_live_pay_order_stat_cost_by_author_3days",
            "luban_live_pay_order_count_by_author_7days",
            "luban_live_pay_order_stat_cost_by_author_7days",
            "luban_live_pay_order_count_by_author_15days",
            "luban_live_pay_order_stat_cost_by_author_15days",
            "luban_live_pay_order_count_by_author_30days",
            "luban_live_pay_order_stat_cost_by_author_30days",
            "total_play",
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
            "ies_challenge_click",
            "ies_music_click",
            "location_click",
            "play_duration_3s",
            "click_call_cnt",
            "click_counsel",
            "coupon_addition",
            "form_click_button",
            "shake_count",
            "attach_creative_show_cnt",
            "attach_creative_click_cnt",
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
            "stat_union_ltv_0",
            "stat_union_ltv_3",
            "stat_union_ltv_7",
            "union_roi_0",
            "union_roi_3",
            "union_roi_7",
            "wechat",
            "submit_certification_count",
            "approval_count",
            "first_order_count",
            "first_rental_order_count",
            "commute_first_pay_count",
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
            "loan_rate"
        ],
        "cascade_fields": [
            "ad_status",
            "landing_type",
            "campaign_name",
            "advertiser_name",
            "ad_budget",
            "ad_bid",
            "ad_deep_cpa_bid",
            "ad_id",
            "ad_external_action",
            "ad_deep_external_action",
            "group_id"
        ],
        "filter": {
            "advertiser": {

            },
            "campaign": {
                "campaign_status": [
                    1
                ]
            },
            "ad": {
                "ad_status": [
                    0
                ]
            },
            "group": {

            }
        }
    }
    response = requests.request(
        method='GET',
        url=url,
        headers=headers,
        json=data,
        allow_redirects=False,
        timeout=time_out
    )
    return response.json()


def ad_promote_ad_list(
        aadvid,
        cookie: str,
        csrf_token: str,
        page: int = 1,
        limit: int = 20,
        time_out: int = 5,
        start_time: datetime.date = time_box.get_relative_date(0),
        end_time: datetime.date = time_box.get_relative_date(0),
        sort_stat: str = 'create_time',
        sort_order: int = 1
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
        "Connection": "keep-alive",
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
        "fields": [
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
        ],

    }
    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        json=data,
        allow_redirects=False,
        timeout=time_out
    )
    return response.json()
