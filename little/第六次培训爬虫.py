import requests
from lxml import etree
import json

base_url = "https://www.douban.com/doulist/1253915/?start="
postfix = "&sort=seq&playable=0&sub_type="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}

if __name__ == "__main__":

    response = requests.get(url = base_url , headers = headers).text
    html = etree.HTML(response)
    context = html.xpath('//*[@id="item277959993"]/div/div[1]')
    for video in context[1:]:
        print(video)
        break