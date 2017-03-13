import os
from bs4 import BeautifulSoup
import codecs
import re
import requests

#拉勾网全国站python分类网址
furl='https://www.lagou.com/zhaopin/Python/?filterOption=3'

#模拟浏览器
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

def download_url(url):
    r=requests.get(url,headers=headers).content
    return r

def crawler(download):
    soup=BeautifulSoup(download)

    job=[]
    company=[]
    location=[]
    require=[]
    information=[]

    contentcontainer=soup.find('div',attrs={'id':'content-container'})

    spositionlist=contentcontainer.find('div',attrs={'class':'s_position_list','id':'s_position_list'})

    sub_list = spositionlist.find('ul',attrs={'class':'item_con_list'}).find_all('li')
    allpage=contentcontainer.find('div',attrs={'class':'pager_container'}).find_all('a')

    #自动查找下一页所需要的url 当到达最后一页时停止
    if not allpage[-1]['href']=='javascript:;':
        nextpage = 'https:'+allpage[-1]['href']
    else:
        nextpage=None

    for each_list in sub_list:
        jo=each_list.find('div',attrs={'class':'p_top'}).find('h2').text
        lo=each_list.find('span',attrs={'class':'add'}).find('em').text
        req=each_list.find('div',attrs={'class':'li_b_l'}).text.replace(' ','').replace('\n',' ')
        co=each_list.find('div',attrs={'class':'company_name'}).find('a').text
        info=each_list.find('div',attrs={'class':'industry'}).text.replace('\n','').replace(' ','')

        job.append(jo)
        location.append(lo)
        require.append(req)
        company.append(co)
        information.append(info)

    return job,location,require,company,information,nextpage


def main():
    url=furl

    if not os.path.exists('/home/xuyang/PycharmProjects/爬虫文件汇总'):
        os.mkdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    os.chdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    with codecs.open('拉钩python招聘信息.txt','wb',encoding='utf-8') as f:
        while url:
            download = download_url(url)
            resj, resl, resr, resc, resi, nextpage = crawler(download)
            url = nextpage
            final = [[a, b, c, d, e] for a, b, c, d, e in zip(resj, resl, resr, resc, resi)]
            for i in final:
                f.write('职位：%s  地区：%s  薪资要求：%s  公司名：%s 公司概况：%s\n\n' % (i[0], i[1], i[2], i[3], i[4]))

if __name__=='__main__':
    main()