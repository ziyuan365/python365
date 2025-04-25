import requests
from bs4 import BeautifulSoup

def get_html(url):
    """获取网页HTML"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None

def parse_html(html):
    """解析HTML内容"""
    if not html:
        return None
        
    soup = BeautifulSoup(html, 'lxml')
    # 示例：提取所有链接
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main():
    """主函数"""
    url = input("请输入要爬取的网址: ")
    html = get_html(url)
    if html:
        results = parse_html(html)
        print(f"找到 {len(results)} 个链接:")
        for link in results[:10]:  # 只显示前10个结果
            print(link)

if __name__ == '__main__':
    main()
