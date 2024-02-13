import requests
url = "http://www.baidu.com"
response = requests.get(url)
# # 打印目前编码格式
# print(response.encoding)
# # 手动设定编码格式
# response.encoding = 'utf8'
# # 打印源码的str类型数据
# print(response.text)
# print(response.encoding)
# response.content是存储的bytes类型源码，可以进行decode操作
print(response.content.decode())

# # 常见的响应对象参数和方法
# # 响应url
# print(response.url)
# # 状态码
# print(response.status_code)
# # 响应对应的请求头
# print(response.request.headers)
# # 响应头
# print(response.headers)
# # 答应响应设置cookies
# print(response.cookies)