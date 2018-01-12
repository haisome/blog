#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,csv,random,os
from .models import UserProfile,MideaUserProfile,MideaUserGroup,EffCard

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def addemployee(groupid, jid, name,sex,email,position,number,py,pyinitials):
    MideaUserProfile.objects.get_or_create(groupid=groupid, jid=jid, name=name,sex=sex,email=email,position=position,number=number,py=py,pyinitials=pyinitials)
    #return db.insert('employee_new', groupid=groupid, jid=jid, name=name,sex=sex,email=email,position=position,number=number,py=py,pyinitials=pyinitials)
def addgroup(parentid, groupid, weight,title):
    MideaUserGroup.objects.get_or_create(parentid=parentid,groupid=groupid,weight=weight,title=title)
    #return db.insert('groups_new', parentid=parentid,groupid=groupid,weight=weight,title=title)

def get_employeecontent():
    return db.select('employee_new', order='id')
def parsefile():
    tree = ET.ElementTree(file='./employee.xml')
    root = tree.getroot()
    #for elem in tree.iter(tag='{urn:xmpp:rooyee:organization:2}items'):
    try:
        count=0
        for elem in root.getchildren():
            groupid= elem.get('groupid','default_value')
            if (elem.tag == '{urn:xmpp:rooyee:organization:2}items'):
                for record in elem:
                    item= record.attrib
                    employee =[groupid,item.get('jid',''),item.get('name',''),item.get('sex',''),item.get('email',''),item.get('position',''),item.get('number',''),item.get('py',''),item.get('pyinitials','')]
                    #cur.execute('insert into employee_new (groupid, jid, name,sex,email,position,number,py,pyinitials) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5],employee[6],employee[7],employee[8]))
                    addemployee(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5],employee[6],employee[7],employee[8])
                    count=count+1
                    if (count%1000==0):
                        print ('Add record: ',count)
            elif (elem.tag == '{urn:xmpp:rooyee:organization:2}groups'):
                Traversal(elem)

    except Exception as e :
        print ("Error %s" %e)
def Traversal(record):
    for ones in record:
        one=ones.attrib
        addgroup( record.get('id',''),one.get('id',''),one.get('weight',''),one.get('title',''))
        Traversal(ones)

if __name__ == '__main__':
    parsefile()
