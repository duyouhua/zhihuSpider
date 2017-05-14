# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem 

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class Spider_Record_Item_Pipeline(object):
	def process_item(self, item, spider):
		if item['item']:
			itemlist = item['item']
			for i in itemlist:
				pass
		return DropItem("over record pipeline")

