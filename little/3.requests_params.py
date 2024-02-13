# import requests
# url = 'https://www.baidu.com/s?wd=python'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
# }
# response = requests.get(url , headers = headers)
# with open('baidu.html' , 'wb')as f:
#     f.write(response.content)

import requests
url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
data = {
    'wd' : 'python'
}
response = requests.get(url , headers = headers , params = data)
with open('baidu1.html' , 'wb')as f:
    f.write(response.content)