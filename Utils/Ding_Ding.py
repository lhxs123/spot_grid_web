# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 10:54
# @Author  : grassroadsZ
# @File    : Ding_Ding.py
import json
from datetime import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot
import requests

dingding_token = "SECd5e9c3a918c1c7caf38dacfd86a69f6c23f8b6d04dba3ff1a56cc0e1f222ee5e"
dingding_webhook = "https://oapi.dingtalk.com/robot/send?access_token=523d3b008ce633c4df5f8e3917c9532ff7579939058e39b0f77ec54cda2e0483"


def send_dingding_msg(content):
    """
    :param content:
    :param robot_id:  你的access_token，即webhook地址中那段access_token。例如如下地址：https://oapi.dingtalk.com/robot/
n    :param secret: 你的secret，即安全设置加签当中的那个密钥
    :return:
    """
    try:
        msg = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n" + content + '\n'
        xiaoding = DingtalkChatbot(dingding_webhook, secret=dingding_token)
        xiaoding.send_text(msg=msg)
    except Exception as e:
        print("发送钉钉失败:", e)


if __name__ == '__main__':
    send_dingding_msg("通知:测试一下")
