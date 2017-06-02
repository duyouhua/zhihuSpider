#coding=utf-8
import scrapy
import sys
from scrapy.loader import ItemLoader
import logging
import time
from PIL import Image


reload(sys)
sys.setdefaultencoding( "utf-8" )

class zhihu_data(scrapy.Item):
	data_title = scrapy.Field()
	data_link = scrapy.Field()
	author_name = scrapy.Field()
	author_describe = scrapy.Field()

class zhihuSpider(scrapy.Spider):
	name = "zhihu"
	username = '13817494755'
	password = '1987910'

	cookie = {
 		'd_c0':'AEDCenyoTguPTutKgwY7oav0pwmQ5zX0oVM=|1487037220',
		'_zap':'c5686156-205f-4df0-87ad-ecf8771f4820',
		'q_c1':'18ade8a474bc44feb35c5daee88edf9b|1494493264000|1494493264000',
		'_xsrf':'c0f841f581938792262f8e41802b9a5c',
		'l_cap_id':'YjFmNjBhZWFjZGVlNDM1NDg5ZGExYzNlMWVjZDM0MDk=|1496210288|daf1467a8c5fee538aa9dc41e959c95a8d7a1358',
		'r_cap_id':'MmRmYmFjZDRiZWJmNDRkMzhmNGMwNjZmZjM5NjZkNjg=|1496210288|0200c76daf2430eefc6522f26411d4cf83353117',
		'cap_id':'NTU2MWE0NmQwOWM1NGU4NGJmNTQ5NTJlNTQ4MTVjOTg=|1496210288|f04658c9c21b66a9627a5ab1d77c639caf87d217',
		'__utmt':'1',
		'__utma':'51854390.1809560242.1488160136.1496198640.1496208717.8',
		'__utmb':'51854390.10.10.1496208717',
		'__utmc':'51854390',
		'__utmz':'51854390.1496208717.8.7.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
		'__utmv':'51854390.000--|2=registration_date=20161109=1^3=entry_date=20170511=1__utmb=51854390.10.10.1496208717',
		'__utmc':'51854390',
		'__utmz':'51854390.1496208717.8.7.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
		'__utmv':'51854390.000--|2=registration_date=20161109=1^3=entry_date=20170511=1',
	}

	urls = [
		'https://www.zhihu.com/#signin',
	]

	process_urls = [
		'https://www.zhihu.com/explore',
	]

	itemlist = []

	def start_requests(self):
		for url in self.urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self, response):
		print '_xcrf:'
		self.xcrf = response.css('body > div.index-main > div > div.desk-front.sign-flow.clearfix.sign-flow-simple > div.view.view-signin > form > input[type="hidden"]::attr(value)').extract_first()
		print self.xcrf
		return self.download_captcha()

	def download_captcha(self):
		t = str(int(time.time()*1000))
		captcha_url = 'http://www.zhihu.com/captcha.gif?r='+t+'&type=login'
		print '=====captcha url is ' + captcha_url
		return scrapy.Request(url=captcha_url,callback=self.after_download_captcha)


	def after_download_captcha(self,response):
		print '======download captcha sucess========='
		with open('D:\\python\\captch.img',"wb") as f:
			f.write(response.body)
			f.close()
		im = Image.open('D:\\python\\captch.img')
		im.show()
		self.captcha = raw_input('input the captcha:')
		return scrapy.FormRequest('https://www.zhihu.com/login/phone_num',
			formdata = {
				'_xsrf': '%s' % self.xcrf,
				'password': self.password,
				'captcha':'%s' % self.captcha,
				'phone_num':self.username,
				'remember_me':'true',
			},
			cookies = self.cookie,
			callback =  self.after_login    
		)


	def after_login(self,response):
		print '========login Sucess========'
		with open('D:\\python\\debug.html',"w") as f:
			f.write(response.body)

		for url in self.process_urls:
			return scrapy.Request(url=url,callback=self.spider_start)

	def spider_start(self,response):
		print '========Spider start========'
		dailyhot = response.css('div.tab-panel:nth-child(4) > div:nth-child(1)');  #获取dailyhot的数据
		for item in dailyhot.css('div.explore-feed'):
			self.itemlist.append(self.parse_item(item))
		for i in self.itemlist:
			pass
		itemdict = {"item":self.itemlist,}    #parse只能return 字典或者item或者None
		return itemdict

	def parse_item(self,item_selector):
		l = ItemLoader(item=zhihu_data(), selector=item_selector)
		l.add_css('data_link','h2 a::attr(href)')
		l.add_css('data_title','h2 a::text')
		if item_selector.css('div.zm-item-answer-author-info a::text').extract_first() is not None:
			l.add_css('author_name','div.zm-item-answer-author-info a::text')
		else:
			l.add_value('author_name','zhihu_user')
		l.add_css('author_describe','div.zm-item-answer-author-info span::attr(title)')
		return l

    	


	
