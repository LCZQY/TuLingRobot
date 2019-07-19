# -*- coding=utf-8 -*-
import requests
import itchat 
import sys
import time
import logging
import json

logger =  logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# handler 输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建 logging format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

keyArry = ["6eab1415e7614855886ab65597dbfa85","7c5b6a401bb148a9b183cff552ec364e","647a885071394e158ad63b5c314e37bf","9c2a86d08698434e8de6c0bc9f370da5","7d792dd40dd94a1dbd95bf647f85e9d3"]

#在机器人哪儿换取内容
def context(text,key):
    api_url = 'http://www.tuling123.com/openapi/api' 
    data = {
            'key': key, # 如果这个 apiKey 如不能用，那就注册一次
            'info': text,  # 这是我们从好友接收到的消息 然后转发给图灵机器人
            'userid': 'wechat-robot', # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json() # 把data数据发
    return r.get('text')

def get_response(msg): 
    #logger.info(json.dumps(msg)+"----------------------------")
    #print (RemarkName ,msg["FromUserName"], Name,User, Nic)
    if msg["FromUserName"] != Name["屏幕脏了 　 ༽"]:
        _info = msg["Text"]
        index = 0
        while(index <= len(keyArry)):
            name = RemarkName[msg['FromUserName']] if RemarkName[msg['FromUserName']] == '' else  wangming[msg['FromUserName']]
            logger.info(name +":"+_info)
            text =  context(_info,keyArry[index])            
            if(text == "亲爱的，当天请求次数已用完。" ) :
                index = i+1
                continue
            if(text == "没有就没有，我继续玩我的游戏了~http://t.cn/EtRviOV") :
                text = "[捂脸]"
            time.sleep(1)          
            logger.info("机器人宝宝"+str(index)+"回复:"+text)
            return text            

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return get_response(msg)


if __name__ == '__main__':
    itchat.auto_login() # hotReload = True, 保持在线，下次运行代码可自动登录  hotReload=True    
    friends = itchat.get_friends(update=True)[0:]  #获取自己的UserName
    Name = {}
    RemarkName = {}
    wangming = {}
    RemarkValue = []
    Nic = []
    User = []
    for i in range(len(friends)):
            RemarkValue.append(friends[i]["RemarkName"])
            Nic.append(friends[i]["NickName"]) #存的是微信名称
            User.append(friends[i]["UserName"])
    for i in range(len(friends)):
            Name[Nic[i]] = User[i]
            RemarkName[User[i]] = RemarkValue[i]
            wangming[User[i]] = Nic[i]
    itchat.run()