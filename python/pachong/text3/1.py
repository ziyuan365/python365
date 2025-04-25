from turtledemo.clock import datum

import requests

url="https://fanyi.baidu.com/sug"
s=input("请输入你想要翻译的英文单词")
dat={
    "kw":s
}
# 发送post请求
resp=requests.post (url,data=dat)
print(resp.json()) #将服务器返回的内容处理成jason
resp.close()