# -*- coding:utf-8 -*-
from  xml.dom import  minidom
import json
#pasedata='''<?xml version='1.0' encoding='utf-8'?><soapenv:Envelope xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"><soapenv:Body><ns:getAttendCardrecordResponse xmlns:ns="http://services.webservices.com"><ns:return>[{"c_devname":"生活电器-Midea","c_unitname":"美的控股_关联单位_IT外包资源管理_系统运维_应用维护模块","c_kqdatetime":"2015-10-31 23:08:37"},{"c_devname":"生活电器-Midea","c_unitname":"美的控股_关联单位_IT外包资源管理_系统运维_应用维护模块","c_kqdatetime":"2015-10-31 18:15:12"},{"c_devname":"生活电器-Midea","c_unitname":"美的控股_关联单位_IT外包资源管理_系统运维_应用维护模块","c_kqdatetime":"2015-10-31 18:11:19"}]</ns:return></ns:getAttendCardrecordResponse></soapenv:Body></soapenv:Envelope>'''
def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''
def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []
def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''

def get_result(filename='CardrecordResponse.xml'):
    doc = minidom.parse(filename)
    root = doc.documentElement
    user_nodes = get_xmlnode(root,'ns:getAttendCardrecordResponse')
    user_list=[]
    for node in user_nodes:
        node_name = get_xmlnode(node,'ns:return')
        cardResponse =get_nodevalue(node_name[0])
        cardResponsejson=json.loads(cardResponse)
        return cardResponsejson
'''        for subnode in cardResponsejson:
            #print subnode
            c_devname1 =subnode['c_devname'].encode('utf-8','ignore')
            c_unitname1 = subnode['c_unitname'].encode('utf-8','ignore')
            c_kqdatetime1 =subnode['c_kqdatetime'].encode('utf-8','ignore')
            #user = {}
            #user['c_devname'] , user['c_unitname'] , user['c_kqdatetime'] = (c_devname1 , c_unitname1 , c_kqdatetime1 )
            #user_list.append(user)
        return user_list'''
if __name__ == '__main__':
    print ('cardResponse:',get_result())
