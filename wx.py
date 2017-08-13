#coding:utf-8
from flask import Flask,request,make_response
import receive,reply
import hashlib
import requests
from youdao import translate
from weather import fetch_weather
app = Flask(__name__)

@app.route('/wx',methods=(['GET','POST']))
def hello_wx():
    if request.method == 'POST':
        web_data = request.data
        print web_data   #后台打日志
        recMsg = receive.parse_xml(web_data)
        if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = recMsg.Content
            print content
            if '0' == content[0] :
                try:
                    translation = ''
                    explains = ''
                    word = content[1:].lstrip()
                    result = translate(word)
                    if result.has_key('translation'):
                        translation = ','.join(result['translation'])
                    if result.has_key('basic'):
                        explains = ','.join(result['basic']['explains'])

                    back_content = translation + '\n' + explains
                    replyMsg = reply.TextMsg(toUser, fromUser, back_content.encode('utf-8'))
                    return replyMsg.send()
                except:
                      replyMsg = reply.TextMsg(toUser, fromUser,'这个真没有。。。')
                      return replyMsg.send()
            elif '1' == content[0]:
                try:
                    city = content[1:].lstrip()
                    wealth_info = fetch_weather(city)
                    day = wealth_info[0]
                    content = 'tomorrow:'  + day['text_day'] + 'high:' +day['high'] + 'low:' + day['low']     
                    replyMsg = reply.TextMsg(toUser,fromUser,content.encode('utf-8'))
                    return replyMsg.send()     
                except:
                     replyMsg = reply.TextMsg(toUser, fromUser,'查询天气失败了 泪奔。。。')
                     return replyMsg.send()

            else:
                 replyMsg = reply.TextMsg(toUser, fromUser,'机器人正在睡觉，没空搭理你哟，哈哈哈')
                 return replyMsg.send()  
        else:
            print "GET Request"
            return "success"
    else:
        print '暂不处理'
        return 'success' 

@app.route('/')
def hello_home():
    return '<h1>刘昊的网站首页。。。持续开发中，敬请期待！！！</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=False)



    
    # data = request.args
    # signature = data.get('signature','')
    # timestap = data.get('timestamp','')
    # nonce = data.get('nonce','')
    # echostr = data.get('echostr','')
    # token = 'lh941120'
    # print signature
    # print timestap
    # print nonce
    # print echostr
    # print token
    # list = [token,timestap,nonce]
    # list.sort()
    # list_str = ''.join(list)
    # sha1 = hashlib.sha1(list_str)
    # sha1_code = sha1.hexdigest()
    
    # print sha1_code
    # if sha1_code == signature :
    #     return echostr    