#coding=utf-8
import scrapy
import sys
from scrapy.loader import ItemLoader
import logging
import time
from scrapy.conf import settings
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

	cookie = settings['COOKIE']

	urls = [
		'https://www.zhihu.com/#signin',
	]

	process_urls = [
		'https://www.zhihu.com/explore',
		'https://www.zhihu.com/node/ExploreAnswerListV2?params={"offset":%d,"type":"day"}'  #今日最热
	]

	itemlist = []

	def start_requests(self):
		for url in self.urls:
			#yield scrapy.Request(url=url,meta = {'cookiejar' : 1},callback=self.parse)
			yield scrapy.Request(url = url ,cookies = self.cookie,callback = self.after_login)


	###验证码下载验证登录
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
			#cookies = self.cookie,
			callback =  self.after_login    
		)

	###########################


	def after_login(self,response):
		print '========login Sucess========'
		count = 0
		for url in self.process_urls:
			if count == 0:
				count = count + 5
				request = scrapy.Request(url=url,cookies=self.cookie,callback=self.spider_start)
				request.meta['type'] = 'first_page'
				yield request
			else:
				newcount = count
				count = count + 5
				request = scrapy.Request(url= url % count,dont_filter=True,cookies=self.cookie,callback=self.spider_start)
				request.meta['type'] = 'dayhot'
				request.meta['count'] = count
				request.meta['listurl'] = url
				yield request

	def spider_start(self,response):
		print '========Spider start========'
		if response.meta['type'] == 'first_page':
			print '++++++++++++first page+++++++++++++++++'
			dailyhot = response.css('div.tab-panel:nth-child(4) > div:nth-child(1)');  #获取dailyhot的数据
			for item in dailyhot.css('div.explore-feed'):
				self.itemlist.append(self.parse_item(item))
		elif response.meta['type'] == 'dayhot':
			if len(response.css('div.explore-feed')) == 0:
				print '==============It is over=================== ',response.meta['count']
				return 
			print '++++++++++++dayhot page+++++++++++++++++'
			for item in response.css('div.explore-feed'):
				self.itemlist.append(self.parse_day_hot_item(item))
			request = scrapy.Request(url=response.meta['listurl'] % response.meta['count'],dont_filter=True,cookies=self.cookie,callback=self.spider_start)
			request.meta['type'] = 'dayhot'
			request.meta['count'] = response.meta['count'] + 5
			request.meta['listurl'] = response.meta['listurl']
			print 'new url is ', request.meta['listurl'] % request.meta['count']
			yield request
		itemdict = {"item":self.itemlist,}    #parse只能return 字典或者item或者None
		yield itemdict


	def parse_day_hot_item(self,item_selector):
		l = ItemLoader(item=zhihu_data(),selector=item_selector)
		#print "url=====",item_selector.css('div.zm-item-answer link::attr(href)').extract_first().encode("utf-8")
		#print 'name=====',item_selector.css('div.answer-head > div.zm-item-answer-author-info > span > span.author-link-line > a::text').extract_first().encode("utf-8")
		#print "describe=====",item_selector.css('div.answer-head span.bio::text').extract_first().encode("utf-8")
		if item_selector.css('div.zm-item-answer link::attr(href)').extract_first() is not None:
			l.add_css('data_link','div.zm-item-answer link::attr(href)')
		else:
			l.add_value('data_link','no_link')
		if item_selector.css('h2 a::text').extract_first() is not None:
			l.add_css('data_title','h2 a::text')
		else:
			l.add_value('data_title','no_title')
		if item_selector.css('div.answer-head > div.zm-item-answer-author-info > span > span.author-link-line > a::text').extract_first() is not None:
			l.add_css('author_name','div.answer-head > div.zm-item-answer-author-info > span > span.author-link-line > a::text')
		else:
			l.add_value('author_name','zhihu_user')
		if item_selector.css('div.answer-head span.bio::text').extract_first() is not None:
			l.add_css('author_describe','div.answer-head span.bio::text')
		else:
			l.add_value('author_describe','zhihu_describe')
		return l


	def parse_item(self,item_selector):
		l = ItemLoader(item=zhihu_data(), selector=item_selector)
		l.add_css('data_link','h2 a::attr(href)')
		l.add_css('data_title','h2 a::text')
		if item_selector.css('div.zm-item-answer-author-info a::text').extract_first() is not None:
			l.add_css('author_name','div.zm-item-answer-author-info a::text')
		else:
			l.add_value('author_name','zhihu_user')
		if item_selector.css('div.zm-item-answer-author-info span::attr(title)').extract_first() is not None:
			l.add_css('author_describe','div.zm-item-answer-author-info span::attr(title)')
		else:
			l.add_value('author_describe','zhihun_describe')
		return l

    	


	
