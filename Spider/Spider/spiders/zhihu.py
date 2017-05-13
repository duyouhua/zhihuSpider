#coding=utf-8
import scrapy
from scrapy.loader import ItemLoader

class zhihu_data(scrapy.Item):
	#user_name = scrapy.Field()
	#user_describe = scrapy.Field()
	data_title = scrapy.Field()
	data_link = scrapy.Field()

class zhihuSpider(scrapy.Spider):
	name = "zhihu"
	headers = {
		"Accept": "*/*",
	    "Accept-Encoding": "gzip,deflate",
	    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
	    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
	    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
	    "Referer": "http://www.zhihu.com/",
    }

	itemlist = []

	def start_requests(self):
		urls = [
			'https://www.zhihu.com/explore',
		]
		for url in urls:
			yield scrapy.Request(url=url,headers=self.headers,callback=self.parse)


	def parse(self, response):
		dailyhot = response.css('div.tab-panel:nth-child(4) > div:nth-child(1)');  #获取dailyhot的数据
		for item in dailyhot.css('div.explore-feed'):
			self.itemlist.append(self.parse_item(item))
		for i in self.itemlist:
			print '===================='
			print i.load_item()['data_title']
			print i.load_item()['data_link']
			print '....................'
		itemdict = {"item":self.itemlist,}    #parse只能return 字典或者item或者None
		return itemdict
	
	def parse_item(self,item_selector):
		l = ItemLoader(item=zhihu_data(), selector=item_selector)
		l.add_css('data_link','h2 a::attr(href)')
		l.add_css('data_title','h2 a::text')
		return l

    	


	
