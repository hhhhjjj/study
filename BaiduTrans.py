# coding=utf8

import httplib
import md5
import urllib
import random
import json


def transByHttpRequest(fromLanguage, toLanguage, queto):
    appid = '20170512000047153'
    secretKey = 'BlWllKkDwU5Wigp07MlR'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid + queto + str(salt) + secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
        queto) + '&from=' + getLanguage(fromLanguage) + '&to=' + getLanguage(toLanguage) + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        resultArray = json_obj['trans_result']
        mylists = []
        for item in resultArray:
            dst  = item['dst']
            mylists.append(dst)
        return mylists
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


def getLanguage(index):
    if index==0:
        return 'zh'
    elif index==1:
        return 'en'
    return 'zh'