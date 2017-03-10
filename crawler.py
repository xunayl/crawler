import re
from bs4 import BeautifulSoup
import requests
import codecs
import os
#页面地址
furl='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?type=S'
temp='https://book.douban.com'
#伪装浏览器的头
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

#下载页面内容
def download_url(url):
    return requests.get(url,headers=headers).content

#爬虫部分
def crawler(download):
    #用bs解析下载下来的页面内容
    soup=BeautifulSoup(download)

    #创建一个列表用来存储内容
    storage=[]

    #第一步找到内容部分
    step_content=soup.find('div',attrs={'id':'content'})

    #第二步找到总列表部分
    step_subjectlist=step_content.find_all('li')

    #由于该网页会提供不存在小说名的空页面，通过find_all没有找到目标时返回空列表进行判断是否到达了空页面
    if not step_subjectlist==[]:
        # 解析出每一个的信息
        for each_li in step_subjectlist:
            text = each_li.find('h2').find('a')['title']
            storage.append(text)

        # 解析下一页的地址
        next_page = soup.find('span', attrs={'class': 'next'}).find('a')
        #find没有找到目标时返回None
        if next_page:
            return storage, temp + next_page['href']
        return storage, None
    return storage, None

def main():
    url=furl

    if not os.path.exists('/home/xuyang/PycharmProjects/爬虫文件汇总'):
        os.mkdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    os.chdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    with codecs.open('豆瓣小说排行-评价.txt','wb',encoding='utf-8') as f:
        while url:
            download=download_url(url)
            novel,url=crawler(download)
            f.write(u'{novel}\n'.format(novel='\n'.join(novel)))


if __name__=='__main__':
    main()

