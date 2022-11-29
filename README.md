# oceanengine
![](https://img.shields.io/badge/Python-3.8.6-green.svg)
![](https://img.shields.io/badge/lazysdk-0.0.21-blue.svg)

#### 介绍
巨量引擎接口封装工具集，含广告回传功能

巨量各系统地址：
```text
巨量引擎官网 https://oceanengine.com/?source=nav_portal
巨量纵横 https://business.oceanengine.com/?source=nav_portal
巨量广告平台 https://ad.oceanengine.com/?source=nav_portal
巨量开放平台 https://ad.oceanengine.com/openapi/index.html?source=nav_portal
群峰服务市场 https://fuwu.oceanengine.com/?source=nav_portal
巨量学 https://school.oceanengine.com/?source=nav_portal
巨量星图 https://star.toutiao.com/?source=nav_portal
巨量创意 https://cc.oceanengine.com/?source=nav_portal
巨量算数 https://trendinsight.oceanengine.com/?source=nav_portal
穿山甲 https://www.pangle.cn/?source=nav_portal
DOU+ https://doujia.douyin.com/delivery?dou_plus_compaign_name=DOU%2B+id%3A+5819&dou_plus_content=%7B%22version%22%3A%22v2%22%7D&dou_plus_medium=oceanengine-channel&dou_plus_medium_id=pc-page-button&dou_plus_source=site&dou_plus_sub_source=inside_media
企业号 https://renzheng.douyin.com/api/welcome/?fiji_source=nav_portal
星图即合 https://www.xingtu.cn/landing?site=creative&utm_source=creative_oceanengine&utm_medium=product_matrix
巨量引擎方舟 https://agent.oceanengine.com/
```

#### 软件架构
- oceanengine.ad
  - 说明：host为 ad.oceanengine.com 的接口
- oceanengine.ad_postback
  - 说明：广告回传功能封装
- oceanengine.business
  - 说明：host为 business.oceanengine.com 的接口
- oceanengine.e
  - 说明：host为 e.oceanengine.com 的接口


#### 安装教程

1.  pip安装
```shell script
pip3 install oceanengine
```
2.  pip安装（使用阿里镜像加速）
```shell script
pip3 install oceanengine -i https://mirrors.aliyun.com/pypi/simple
```

#### 使用说明

1.  demo
```python
import oceanengine
test_res = oceanengine.ad.promote_ad_list(cookie='cookie', csrf_token='token', aadvid='')
```
