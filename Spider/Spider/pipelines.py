# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem 
import logging

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class Spider_Record_Item_Pipeline(object):
	def process_item(self, item, spider):
		if item['item']:
			itemlist = item['item']
			for i in itemlist:
				logging.log(logging.INFO,'====================')
				logging.log(logging.INFO,'%s',i.load_item()['author_name'][0])
				logging.log(logging.INFO,"%s",i.load_item()['author_describe'][0])
				logging.log(logging.INFO,"%s",i.load_item()['data_link'][0])
				logging.log(logging.INFO,"%s",i.load_item()['data_title'][0])
				logging.log(logging.INFO,'....................')
		return DropItem("over record pipeline")

