#coding=utf-8
import json
from urllib import request,parse
'''import sys
reload(sys)
sys.setdefaultencoding("utf8")'''
def tuling(ask):
    #enask = ask.encode('UTF-8')
    #enask = urllib2.quote(ask)
    posturl = 'http://openapi.tuling123.com/openapi/api/v2'
    headers = {'Host': 'openapi.tuling123.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 (374348800)',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8'
    }
    postdata='''{
    "perception": {
        "inputText": {
            "text": "%s"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "latitude": "39.45492",
                "longitude": "119.239293",
                "nearest_poi_name": "上地环岛南",
                "province": "北京",
                "street": "信息路"
            },
        }
    },
    "userInfo": {
        "apiKey": "fac1c9633dd1439993f4453e26283108",
        "userId": 1
    }
}'''%ask
    postdata = postdata.encode(encoding='UTF8')
    print (postdata)
    req = request.Request(posturl,postdata,headers)
    resp = request.urlopen(req)
    content = resp.read().decode('utf-8')
    if(content):
        print (content)
        content = str(content).replace("'", '"')
        #return content
        content =json.loads(content)['results']
        for line in content:
            if line['resultType']=='text':
                return line['values']['text']
if __name__ == "__main__":
    print (tuling('天气如何'))
