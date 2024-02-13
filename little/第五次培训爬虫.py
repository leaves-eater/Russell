import requests

# url = 'https://ssr1.scrape.center/detail/1'
# response = requests.get(url = url)
#
# page_text = response.text
# print(page_text)
# print("爬行数据结束。。。")

# r = requests.get("https://httpbin.org/get?name=germey&age=22")
# text = r.text
# print(text)

#伪装成浏览器发送请求
# import re
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/105.0.0.0 '
#                          'Safari/537.36 Edg/105.0.1343.42'}
# r = requests.get(url:"https://www.zhihu.com/explore",headers=headers)
# pattern = re.compile(pattern)

# url = 'https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c'
# img_data = requests.get(url = url).content
# with open('./img.jpg','wb')as fp:
#     fp.write(img_data)

# from lxml import etree
#
# text = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1">second item</li>
#          <li class="item-inactive">third item</li>
#          <li class="item-1">fourth item</li>
#          <li class="item-0">fifth item
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[@class="item-1"]/text()')
# result = html.xpath('/div/ul/li[1]/a/text()')
# print(result)
from lxml import etree

url = 'https://ssr1.scrape.center/detail/1'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/105.0.0.0 '
                         'Safari/537.36 Edg/105.0.1343.42'}

page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
#print(page_text)

# result = tree.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p/text()')
# print(result[0])

title = tree.xpath('//div[@class = "p-h el-col el-col-24 el-col-xs-16 el-col-sm-12"]/a/h2/text()')
print(title)