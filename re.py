#-*-  coding:utf8 -*-

import os
import urllib2  
import hashlib  
import json  
import random
from urllib import urlretrieve
import urllib
import urlparse
import sys

class BacthRename():
	"""docstring for BacthRename"""
	def __init__(self):
		self.path = os.getcwd(); 


	def rename(self):
		
		filelist = os.listdir(self.path);
		total_num = len(filelist);
		i = 0;

		for item in filelist:
			if not item.endswith('.jpg') and not item.endswith('.png'):
				continue
			src = os.path.join(os.path.abspath(self.path), item)
			(filepath,tempfilename) = os.path.split(item)
			(shotname,extension) = os.path.splitext(tempfilename)
			englishName = self.getResult(shotname)
			rename  = englishName.encode("utf-8")
			rename1 = rename.replace(" ","_").lower()
			if item.endswith('.jpg'):
				dst = os.path.join(os.path.abspath(self.path), rename1 + '.jpg');
			elif item.endswith('.png'):
				dst = os.path.join(os.path.abspath(self.path), rename1 + '.png');
			try:
				print item[:-4] + '----->' + rename1 + '\n'
				os.rename(src, dst);
			except: 
				continue;
  
  	def deleteAt(self,imageName):
  		if imageName.endswith("@3x") or imageName.endswith("@2x"):
  			return imageName[:-3]
  		return imageName

  	def addAt(self,subName,resultName):
  		if resultName.endswith("@3x"):
  			return subName + '@3x'
  		elif resultName.endswith("@2x"):
  			return subName + '@2x'
  		return subName

  		
  		
	def getResult(self,strNmae):  
		url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
		data = {}
		data['type'] = 'AUTO'
		data['i'] = self.deleteAt(strNmae)
		data['doctype'] = 'json'
		data['xmlVersion'] = '1.8'
		data['keyfrom'] = 'fanyi.web'
		data['ue'] = 'UTF-8'
		data['action'] = 'FY_BY_CLICKBUTTON'
		data['typoResult'] = 'true'
		data = urllib.urlencode(data).encode('utf-8')
		response = urllib.urlopen(url, data)
		html = response.read().decode('utf-8')
		target = json.loads(html)
		results = target['translateResult'][0][0]['tgt']
		finalRes = results
		 
		return self.addAt(results,strNmae)
		

if __name__ == '__main__':
	demo = BacthRename();
	demo.rename();