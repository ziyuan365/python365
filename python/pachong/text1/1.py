from urllib.request import urlopen
import os

# 获取当前脚本的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

url = "http://www.baidu.com/"
resp = urlopen(url)

# 读取响应内容并保存到变量中
content = resp.read().decode("utf-8")

# 构建文件的完整路径
file_path = os.path.join(script_dir, "mybaidu.html")

# 将内容写入文件
with open(file_path, mode="w", encoding="utf-8") as f:
    f.write(content)

print("over!")
resp.close()