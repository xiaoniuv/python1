import requests
import re
from bs4 import BeautifulSoup

def getHtml(url,headers,cookies):
    try:
        r = requests.get(url,headers = headers, cookies = cookies)
        r.raise_for_status
        print(r)
        print(r.headers)
        # print(r.raise_for_status)
        # print(r.text)
        print(r.encoding)
        r.encoding = r.apparent_encoding
        content_type = r.headers['content-type']
        print(content_type)

        return  r.text
    except:
        print("爬取失败！")

def main():
    url = "https://fishc.com.cn/"
    headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    cookies = {
    'oMVX_2132_nofavfid': '1',
    'oMVX_2132_smile': '5D1',
    'oMVX_2132_nofocus_forum': '1',
    'oMVX_2132_saltkey': 'cmZ93PLQ',
    'oMVX_2132_lastvisit': '1585139944',
    'oMVX_2132_atarget': '1',
    'oMVX_2132_visitedfid': '243D173D38D360D319',
    'oMVX_2132_forum_lastvisit': 'D_360_1584665521D_38_1585036065D_173_1585184232D_243_1585184316',
    'acw_tc': '781bad0915852757354621672e18dec3e9e1a476502342a07c8fa830f62a72',
    'oMVX_2132_ulastactivity': '4cd3TZfmkAK0UiV%2FfZdP39%2BtOPP0atM%2BL1guLqES8ASm3qy3RqoC',
    'oMVX_2132_auth': 'd036JvI7ZK4aP6B%2BY3etfWgYAJOhmmqUMmJLYV3XK8vL7YAqDQxNcX7YH1lapvuodApw1ks%2BoJgtLK5rochZIuoiAro',
    'oMVX_2132_lastcheckfeed': '717823%7C1585275753',
    'PHPSESSID': 'b20qg3p6bg0ij67djoimni8jb6',
    'oMVX_2132_sid': 'K96PUl',
    'oMVX_2132_lip': '111.112.156.87%2C1585275753',
    'oMVX_2132_noticeTitle': '1',
    '_fmdata': 'UhW0nG%2Bbg4WgCi4b2QALOSVHEQ%2FkH4XudZ6V9khUzicFuCfHcb5qr%2BPHQoMQQZ7dhzcArJfzh%2BtJs6I2gU1LeaJIURSoXr8vpXHE9MTplp8%3D',
    'oMVX_2132_lastact': '1585277270%09misc.php%09patch',
    }

    html = getHtml(url,headers,cookies)
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)

    ul = soup.find('meta')
    print(ul)
    um = ul.attrs['content']
    print(um)
    print(type(um))



main()


