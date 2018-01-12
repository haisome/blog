#!/usr/bin/python
#coding:utf-8
import urllib.parse,urllib.request
import string,datetime,sys
import re,demjson,http.cookiejar
import json,csv
from .parsehistory import *
#登录的主页面
hosturl = 'http://login.midea.com/' #自己填写
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'https://login.midea.com/logincom/addMideaSSOToken.json' #从数据包中分析出，处理post请求的url
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
#h = urllib.urlopen(hosturl)
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Host': 'login.midea.com',
}
#构造Post数据，他也是从抓大的包里分析得出的。
#postData = '''username=ex_penglei&auth=0&password=Leo0120'''
#需要给Post数据编码
#postData = urllib.urlencode(postData)
#postData = json.dumps(postData,skipkeys=True)
#print postData
#通过urllib提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
def getToken(username,password):
    postData = '''username={0}&auth=0&password={1}'''.format(username,password)
    #postData=urllib.parse.urlencode(postData)
    postData=postData.encode('utf-8')
    request = urllib.request.Request(posturl, postData, headers)
    response = opener.open(request)
    text = response.read()
    #text='test'
    #text = json.dumps(text,indent=4)
    #print text
    #f=open('./login.txt','w+')
    #f.write(text)
    #f.close()
    text=demjson.decode(text)
    print (text)
    midea_sso_token=''
    for item in cookie:
        #print item.name,'=',item.value
        if item.name=='midea_sso_token':
            midea_sso_token=item.value
    print ("midea_sso_token=",midea_sso_token)
    return [text,midea_sso_token]

def writessotoken(midea_sso_token):
    f=open('./ssotoken.txt','w+')
    f.write(midea_sso_token)
    f.close()
midea_sso_token='''uhFOo%2BGSjeiGGvXpOgvZ5RYt75PmFRAvR%2FaiYC30M5xn6sYirvv1V%2F47B%2BmtjTlP'''
date=datetime.datetime.now().strftime('%Y-%m-%d')
moveCardOid=437802
cardNum=11326418#11193553#11326421
count=0
getAttendCardrecord='http://mas.midea.com/pre.do?alias=ic.meixin.getAttendCardrecord&empId=%s&MipType=0&midea_sso_token=%s&MipDatetime=%s'
queryEffCard='http://mas.midea.com/pre.do?&alias=ic.meixin.queryEffectiveCardPoint&latitude=22.914522&longitude=113.206657&param=%s&type=0&midea_sso_token=%s&test=%s'
addMoveCard='http://mas.midea.com/pre.do?&alias=ic.meixin.addMoveCard&param=%s&midea_sso_token=%s&type=0&cardType=1&moveCardOid=%s'
def doGet(gettype,urlGet,cardNum,midea_sso_token,three):
    midea_sso_token = urllib.request.quote(midea_sso_token)
    urlrealGet=urlGet%(cardNum,midea_sso_token,three[0])
    headers = {
    'Accept': 'ext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    }
    print (urlrealGet)
    req = urllib.request.Request(url=urlrealGet,headers=headers)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    #print 'cardNum=',cardNum
    #打印获取的内容
    #print res.decode('utf8').encode('gbk')
    #global count
    #count=count+1
    #if count==3:
    #    return 'try 3 times'
    #f=open('./getresult.txt','wb+')
    #f.write(res)
    #f.close()
    #print 'write succuss\n'
    if gettype=='queryEffCard':
        res = demjson.decode(res)
        print (res)
        if res.get('result','default_value')==-1:
            result=getToken(three[0],three[1])
            midea_sso_token=result[1]
            doGet('queryEffCard',urlGet,cardNum,midea_sso_token,three[0])
            #return -1
        result = res['resultList']
        #for item in result:
            #print 'distance:',item['distance'],'cardName:',item['cardName'],'oid:',item['oid'],'longitude:',item['longitude'] ,'latitude:',item['latitude'] ,'cardRadius:',item['cardRadius'] ,'applyDate:',item['applyDate']
        #    print ('oid:',item['oid'],'cardName:',item['cardName'])
        return result
    elif gettype=='addMoveCard':
        res = demjson.decode(res)
        if res.get('flag','default_value')!="1":
            result=getToken(three[0],three[1])
            midea_sso_token=result[1]
            doGet('addMoveCard',urlGet,cardNum,midea_sso_token,three)
        else:
            print ('GPS打卡成功')
    elif gettype=='getAttendCardrecord':
        '''for subnode in get_result(filename='./getresult.txt'):
            #print subnode
            c_devname1 =subnode['c_devname']
            c_unitname1 = subnode['c_unitname']
            c_kqdatetime1 =subnode['c_kqdatetime']
            print (c_devname1,c_unitname1,c_kqdatetime1)'''
        return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        cardNum = sys.argv[1]
    else :
        cardNum=input("输入打卡工号：")
    try :
        doGet('queryEffCard',queryEffCard,cardNum,midea_sso_token,['ex_penglei','Leo0120'])
        #oid=input("输入打卡点oid：")
        #doGet('addMoveCard',addMoveCard,cardNum,midea_sso_token,oid)
        doGet('getAttendCardrecord',getAttendCardrecord,int(cardNum),midea_sso_token,date)
    except Exception as e:
         print (e)
