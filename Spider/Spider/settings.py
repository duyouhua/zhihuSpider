# -*- coding: utf-8 -*-

# Scrapy settings for Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWe bKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# 				"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
# 				"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
# 				"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
# 				"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
# 				"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
# 				"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
# 				"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
# 				"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
# 				"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
# 				"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
# 				"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
# 				"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
# 				"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
# 				"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
# 				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
# 				"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
# 			]

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# PROXIES = [
# 	{'ip_port': '125.89.123.198:808', 'user_pass': ''},
# 	{'ip_port': '59.37.22.82:3128', 'user_pass': ''},
# 	{'ip_port': '171.38.213.78:8123', 'user_pass': ''},
# 	{'ip_port': '115.203.82.131:808', 'user_pass': ''},
# 	{'ip_port': '180.121.164.159:35251', 'user_pass': ''},
# 	{'ip_port': '122.224.249.122:8088', 'user_pass': ''},
# ]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIE = {	'q_c1': '18ade8a474bc44feb35c5daee88edf9b|1494493264000|1494493264000', 
			'__utmz': '51854390.1496392035.3.3.utmcsr', 'z_c0': 'Mi4wQURCQUFsTVcwZ29BUU1KNmZLaE9DeGNBQUFCaEFsVk5DVlJjV1FEUzRYSlo1Yjh0ejBSTmJSY1BIWnlVSVRyTDJB|1496631049|8315af87b3e602f65edb0bacfa3241cd00f3de19', 
			'_zap': 'c5686156-205f-4df0-87ad-ecf8771f4820',
 '__utmv': '51854390.000--|2', '_xsrf': 'c0f841f581938792262f8e41802b9a5c', 
 'r_cap_id': '"MmY4NGI2ZjgyNjVhNGQyMTkyMjYxMmNhYjcxZDIxYjM', 
 'cap_id': '"NDY5NmYwNzhkNjY4NDE3OGJjNjMwZTFhYjg3NDRlNTA', 
 '__utma': '51854390.652328559.1496369069.1496392035.1496630992.4', 
 'd_c0': '"AEDCenyoTguPTutKgwY7oav0pwmQ5zX0oVM', 
 '__utmc': '51854390', '__utmb': '51854390.0.10.1496630992', }
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#知乎explore今日最热加载数
dayhot = 5

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
	"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Spider.middlewares.SpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#	'Spider.middlewares.RandomUserAgent':1,
 #   'Spider.middlewares.ProxyMiddleware': 100,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Spider.pipelines.Spider_Record_Item_Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
