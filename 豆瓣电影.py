import requests
# import re
# import json
from bs4 import BeautifulSoup


def request_dandan(url):
    headers = {
        # "Referer": "https://movie.douban.com/top250?start=0&filter=",
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": "Windows",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# def parse_result(html):
#     pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">¥(.*?)</span>.*?</li>', re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'range': item[0],
#             'iamge': item[1],
#             'title': item[2],
#             'recommend': item[3],
#             'author': item[4],
#             'price': item[6]
#         }


# def write_item_to_file(item):
#     print('开始写入数据 ====> ' + str(item))
#     with open('book.txt', 'a', encoding='UTF-8') as f:
#         f.write(json.dumps(item, ensure_ascii=False) + '\n')
#         f.close()

def main(page):
    url = 'https://movie.douban.com/top250?start=' + \
        str(25 * (page - 1)) + '&filter='
    html = request_dandan(url)
    soup = BeautifulSoup(html, 'lxml')
    list = soup.find(class_="grid_view").find_all('li')
    for item, index in list:
        print(index)
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        item_intr = item.find(class_='inq').string

        print('爬取电影：' + item_index + ' | ' + item_name +
              ' | ' + item_score + ' | ' + item_intr)


if __name__ == "__main__":
    for i in range(1, 5):
        main(i)
