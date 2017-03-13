import requests
from bs4 import BeautifulSoup
import os
import codecs

url='https://www.baidu.com/'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

def download_url(url):
    r=requests.get(url,headers=headers).content
    return r

def crawler(download):
    soup=BeautifulSoup(download)
    img = soup.find('div', attrs={'id': 'head'}).find('div',attrs={'id':'lg'}).find('img')['src']
    res=requests.get('https:'+img).content
    return res

def main():
    if not os.path.exists('/home/xuyang/PycharmProjects/爬虫文件汇总'):
        os.mkdir('/home/xuyang/PycharmProjects/爬虫文件汇总')
    os.chdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    result=crawler(download_url(url))
    with codecs.open('百度图标.icon','wb') as f:
        f.write(result)

if __name__=='__main__':
    main()