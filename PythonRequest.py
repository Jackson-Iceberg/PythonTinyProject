# @Time: 17/07/2022 00:58
# @Author: Jackson Zhou
import requests

url = 'https://www.baidu.com'
response = requests.get(url=url)
response.encoding = 'utf-8'
print(response.text)
print(response.url)
print(response.content)
print(response.status_code)
print(response.headers)
