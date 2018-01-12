#coding: utf-8

import os
import os.path
rootdir = "/Users/haisome/Documents/python/july/July/static"

for parent,dirnames,filenames in os.walk(rootdir):
	for dirname in  dirnames:
		print "parent is:" + parent
		print  "dirname is:" + dirname

	for filename in filenames:
		print "parent is:" + parent
		print "filename is:" + filename
		print "the full name of the file is:" + os.path.join(parent[14:],filename)
		#print "the path is:" +os.path.abspath('.')
		#print open(os.path.join(parent,filename), "rb").read()
		f=open(os.path.join(parent,filename) ,'rb')
		data=f.read()
		f.close()
		filename=os.path.join(parent[48:],filename)
		print filename
		f=open('./file','wb')
		f.write(data)
		f.close()
		os.rename('file',filename)
		f=open('./file','wb')
		f.write(data)
		f.close()
