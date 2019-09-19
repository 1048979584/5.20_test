#parsel是scrapy的内置选择器包含re、css、xpath选择器依赖xml
import requests
from parsel import selector
import requests

url = "https://newes.baidu.com/"
body=requests.get(url).text
print(body)
selector = selector(text=body)
#xpath
title = selector.xpath("//title/text()").extract_first()
#返回list把所有匹配的值都返回
#title=selector.xpath("//title/text()").extrac()[0]
print(title)

#正则re：
title=selector.re("<title>(\s+)</title)")[0]
print(title)
#css:--title标签的文本
title=selector.css("title::text").extract_first()
print(title)

#re和xpath结合
title=selector.xpath("//title/text()").re("(\S\S)")[0]
print(title)
#css+re
title=selector.css("title::text").re("(\S\S)")[0]
print(title)

'''爬书实践'''
def getText(url,header):
    response=requests.get(url,headers)
#处理乱码
    response.encoding=response.apparent_encoding
#创建一个parsel选择器对象
    sel=parsel.Selector(response.text)
#css根据属性选择
    title=sel.css('h1::text').get()
#sel对象的使用
    content=sel.css('#content::text').getall()

with open(title+'.txt','w+',encoding='utf-8')as f:
    content1 = ''.join(content).replace('\xa0', '')
    content2 = ''.join(content1).replace('\n', '')
    f.writelines(content2)