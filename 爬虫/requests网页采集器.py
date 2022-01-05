import requests
if __name__ == "__main__":
    url = "https://www.sogou.com/web?"
    kw = input("请输入关键字:")
    param = {
        'query': kw
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    res = requests.get(url, params=param, headers=headers)
    page_text = res.text
    file_name = kw + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print(file_name, '保存成功!')
