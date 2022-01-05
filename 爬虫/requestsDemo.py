import requests

if __name__ == '__main__':

    url = 'https://www.sogou.com'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    # 发起请求
    res = requests.get(url=url, headers=headers, verify=False)
    # 获取响应数据
    page_text = res.text
    print(page_text)
    # 持久话存储
    with open('./sogou.html', 'w', encoding='UTF-8') as f:
        f.write(page_text)
    print('爬取结束')
