import requests
import re
import json
from lxml import etree

class Spider:
    def __init__(self, headers, url, fn, fp=None):
        self.headers = headers
        self.url=url
        self.fn=fn
        self.fp=fp

    def open_file(self):
        #self.fp = open('学习强国2.txt', 'w', encoding='utf8')
        self.fp = open(self.fn, 'w', encoding='utf8')

    def get_data(self):
       return requests.get(url=self.url, headers=self.headers).text

    def parse_home_data(self):
        ex = '".*?url":"(.*?)"'
        home_data=self.get_data()
        return re.findall(ex,home_data)

    def parse_detail_data(self):
        detail_url=self.parse_home_data()
        print(detail_url,flush=True) #即时打印结果
        '''i = 0
        urls = ''
        for url in detail_url:
            i += 1
            urls += '{"url":"' + ''.join(url) + '","producer":"旧PC站"},' #组合成特殊格式
        self.fp.write(urls[:-1])
        print(i)'''
        print(len(detail_url))
        self.fp.write(f'["' + '","'.join(detail_url) + '"]') #构造一个list的文本格式

    def close_file(self):
        self.fp.close()

    def run(self):
        self.open_file()
        self.parse_detail_data()
        self.close_file()

if __name__ == '__main__':
    headers = {
        'Host': 'www.xuexi.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    url0 = 'https://www.xuexi.cn/f997e76a890b0e5a053c57b19f468436/data018d244441062d8916dd472a4c6a0a0b.js' #练习用
    
    url1 = 'https://www.xuexi.cn/lgdata/35il6fpn0ohq.json' #文章数量，成品中需要手工查找lgdata并删除与之相关的网址
    url2 = 'https://www.xuexi.cn/72ac54163d26d6677a80b8e21a776cfa/data9a3668c13f6e303932b5e0e100fc248b.js' #文章时长，成品直接可用
    url3 = 'https://www.xuexi.cn/lgdata/17th9fq5c7l.json' #视频数量，成品直接可用
    url4 = 'https://www.xuexi.cn/a191dbc3067d516c3e2e17e2e08953d6/datab87d700beee2c44826a9202c75d18c85.js' #视频时长，成品直接可用
    
    spider=Spider(url=url0,headers=headers,fn='tmp.txt')
    
    #spider=Spider(url=url1,headers=headers,fn='article_links_new.db') //成品中需要手工查找lgdata并删除与之相关的网址
    #spider=Spider(url=url2,headers=headers,fn='article_links_old.db')
    #spider=Spider(url=url3,headers=headers,fn='video_links_new.db')
    #spider=Spider(url=url4,headers=headers,fn='video_links_old.db')
    
    spider.run()