# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'd_c0="AEDCenyoTguPTutKgwY7oav0pwmQ5zX0oVM=|1487037220"; _zap=c5686156-205f-4df0-87ad-ecf8771f4820; q_c1=18ade8a474bc44feb35c5daee88edf9b|1494493264000|1494493264000; _xsrf=c0f841f581938792262f8e41802b9a5c; r_cap_id="MmY4NGI2ZjgyNjVhNGQyMTkyMjYxMmNhYjcxZDIxYjM=|1496630993|6ce109ef9921cddecb269d97d42f74b6937f9325"; cap_id="NDY5NmYwNzhkNjY4NDE3OGJjNjMwZTFhYjg3NDRlNTA=|1496630993|bf1347e2db19b68b744f1c790913ef44e75e24a4"; __utma=51854390.652328559.1496369069.1496392035.1496630992.4; __utmb=51854390.0.10.1496630992; __utmc=51854390; __utmz=51854390.1496392035.3.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20161109=1^3=entry_date=20170511=1; z_c0=Mi4wQURCQUFsTVcwZ29BUU1KNmZLaE9DeGNBQUFCaEFsVk5DVlJjV1FEUzRYSlo1Yjh0ejBSTmJSY1BIWnlVSVRyTDJB|1496631049|8315af87b3e602f65edb0bacfa3241cd00f3de19'
    trans = transCookie(cookie)
    print trans.stringToDict()