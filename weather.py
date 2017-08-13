# coding:utf-8
import sys
import requests
import zlib
import chardet
import json
from bs4 import BeautifulSoup
import time
import hmac
import hashlib
import base64
import urllib
import urllib2
url = 'http://php.weather.sina.com.cn/search.php'
param = {
    'city':'',
    'dpc':1
}

# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8
# Connection:keep-alive
# Cookie:SINAGLOBAL=1.180.215.130_1495277983.935956; U_TRS1=00000082.fd254c9c.5920556d.ff465564; UOR=www.baidu.com,blog.sina.com.cn,; SUB=_2AkMuPqZuf8NxqwJRmPkdzGPlbYV2zQDEieKYYle1JRMyHRl-yD83qmAstRAcscLmgL-Sb8ElQmy9S9bRyh6E1Q..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWf58xr3yM0W.mjkOeyYliL; U_TRS2=000000d8.74cd5e7d.597d8e2b.ab8bd92f; Apache=36.102.227.216_1501400619.313241; SessionID=o6gvckn2afqeksl27uinp9sl95; vjuids=-393fee38f.15d92764df0.0.857476bf74c1d; ULV=1501400813048:6:5:2:36.102.227.216_1501400619.313241:1501400752247; rotatecount=3; WEB2=44a4ed32ba0babcc2dfe010a6a0d8835; vjlast=1501400813.1501400813.30; tpte=C; lxlrttp=1501326246
# Host:php.weather.sina.com.cn
# Referer:http://weather.news.sina.com.cn/
# Upgrade-Insecure-Requests:1
# User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'SINAGLOBAL=1.180.215.130_1495277983.935956; U_TRS1=00000082.fd254c9c.5920556d.ff465564; UOR=www.baidu.com,blog.sina.com.cn,; SUB=_2AkMuPqZuf8NxqwJRmPkdzGPlbYV2zQDEieKYYle1JRMyHRl-yD83qmAstRAcscLmgL-Sb8ElQmy9S9bRyh6E1Q..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWf58xr3yM0W.mjkOeyYliL; U_TRS2=000000d8.74cd5e7d.597d8e2b.ab8bd92f; Apache=36.102.227.216_1501400619.313241; SessionID=o6gvckn2afqeksl27uinp9sl95; vjuids=-393fee38f.15d92764df0.0.857476bf74c1d; ULV=1501400813048:6:5:2:36.102.227.216_1501400619.313241:1501400752247; rotatecount=3; WEB2=44a4ed32ba0babcc2dfe010a6a0d8835; vjlast=1501400813.1501400813.30; tpte=C; lxlrttp=1501326246',
    'Host':'php.weather.sina.com.cn',
    'Referer':'Referer',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# def get_weather(city = '北京'):
#     global param
#     param['city'] = city
#     response = requests.get(url,params=param,headers = header)
#     weather_html = response.content.decode('GB2312','ignore').encode('UTF-8','ignore')
#     bs = BeautifulSoup(weather_html,'html.parser')
#     wealth_list = bs.select('div.weather_list')
#     wealth_data = wealth_list[0]
#     four_days_data = wealth_data.select('div.mod_02')
#     tomorrow_data = four_days_data[0]
#     detail = tomorrow_data.select('ul')[0]
#     item = detail.select('li')
#     data = ''
#     for info in item:
#         temp = data + info.string + ' '
#         data = temp
    
#     print data

#     return data

app_key = 'smsi7o0yliiq3anm'

def fetch_weather(city='beijing'):
    base_url = 'https://api.seniverse.com/v3/weather/daily.json'
    param = {
        'key':app_key,
        'location':city,
        'language':'zh-Hans',
        'unit':'c',
        'start':0,
        'days':3
    }
    r = requests.get(base_url,params=param) 

    
    # print r.text
    # print r.url
    json_data = r.json()
    array = json_data['results']
    real_data = array[0]
    daily = real_data['daily']
    
    return daily
  



        
    


if __name__ == '__main__':
    # get_weather()
    fetch_weather()