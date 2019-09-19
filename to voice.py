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
if __name__=="__main__":
    print('开始爬取，请稍候...')
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie':'Hm_lvt_3806e321b1f2fd3d61de33e5c1302fa5=1568816590; bcolor=; font=; size=; fontcolor=; width=; Hm_lpvt_3806e321b1f2fd3d61de33e5c1302fa5=1568816903'
    }
    urls=[
        'http://www.shuquge.com/txt/63542/9645081.html',
        'http://www.shuquge.com/txt/63542/9645082.html',
        'http://www.shuquge.com/txt/63542/9645082.html',
        'http://www.shuquge.com/txt/63542/17214480.html',
        'http://www.shuquge.com/txt/63542/17219206.html',
        'http://www.shuquge.com/txt/63542/17220023.html',
        'http://www.shuquge.com/txt/63542/17220374.html',
        'http://www.shuquge.com/txt/63542/17223363.html',
    ] # 将url链接放到列表里面，每次取出一个进行爬取
    for url in urls:
        getText(url,header)
    print('恭喜你，爬取完成。')    
    
    
