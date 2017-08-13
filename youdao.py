# coding:utf-8

import requests
import random
import hashlib
url = 'http://openapi.youdao.com/api'

data = {
   'q':'default',
   'from':'auto',
   'to':'auto',
   'appKey':'7b6c11d9920c7ac0',
   'salt':0,
   'sign':''    
}
  

def translate(word='hello'):
    global data
    data['q'] = word
    salt = random.randint(0,101)
    data['salt'] = salt
    sign = data['appKey'] + data['q'] + str(data['salt']) + 'wIyhDXe5hUCDiBFehnFnWfAEwvxrBZt2'
    md5 = hashlib.md5()
    md5.update(sign)
    
    data['sign'] = md5.hexdigest()

    res = requests.get(url,params=data)
    json_result = res.json()
    translation = ','.join(json_result['translation'])
    explains = ','.join(json_result['basic']['explains'])
    content = translation + '\n' + explains
    return json_result

if __name__ == '__main__':
    translate('welcome')
