import requests
url = "http://www.baidu.com"
# 不加请求头
# response = requests.get(url)
# print(len(response.content.decode()))
# print(response.content.decode())

# 加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
}
response1 = requests.get(url, headers = headers)
print(len(response1.content.decode()))
print(response1.content.decode())