#coding=utf8
'''
import sys
reload(sys)
sys.setdefaultencoding("utf8")
'''
from werobot import WeRoBot
from django.shortcuts import render
from .tuling123 import *
robot = WeRoBot(enable_session=True,
                token='haisome',
                APP_ID='wxb783acbc42704203',
                APP_SECRET='921332a17d545d5e42ca8d115196eb6d')
'''
robot = WeRoBot(enable_session=True,
                token='haisome',
                APP_ID='wx8292bf7c09c22b24',
                APP_SECRET='fb7518ce4fb780cfc2d7097fd71b24b6')
@robot.handler
def hello(message):
    return 'Hello world'
'''
client = robot.client
@robot.subscribe
def subscribe(message):
    return 'Hello My Friend!'
# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def first(message):
    if message.content.startswith(u'创建菜单'):
        client.create_menu({
         "button":[{
         "type": "click",
         "name": "打卡",
         "key": "music"
               }]})
        return u'创建菜单成功'
    elif message.content.startswith(u'打卡'):
        return [
        [
            "今日打卡",
            "description",
            "https://secure.gravatar.com/avatar/0024710771815ef9b74881ab21ba4173?s=420",
            "http://haisong.pythonanywhere.com/"
        ],
    ]

    else:
        return tuling(message.content)

# @robot.image 修饰的 Handler 只处理图片消息
@robot.image
def img(message):
    return message.img
# @robot.location 修饰的 Handler 只处理位置消息
@robot.location
def location(message):
    return message.location
@robot.key_click("music")
def music(message):
    return [
        [
            "今日打卡",
            "description",
            "https://secure.gravatar.com/avatar/0024710771815ef9b74881ab21ba4173?s=420",
            "http://haisong.pythonanywhere.com"
        ],
           ]
@robot.error_page
def make_error_page(url):
    return "<h1>喵喵喵 %s 不是给麻瓜访问的快走开</h1>" % url
