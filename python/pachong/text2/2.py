import requests
import sys
import io

# 设置标准输出的编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
wd=input("输入一个你喜欢的明星")
# 百度搜索 URL
url = f"http://www.baidu.com/s?tn=15007414_15_dg&ie=utf-8&wd={wd}"

# 如果网站有反爬机制 则设置 User-Agent 头
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }                             

# 发送 GET 请求
resp = requests.get(url)

# 打印响应对象
print(resp)

# 打印响应内容
print(resp.text)
resp.close()