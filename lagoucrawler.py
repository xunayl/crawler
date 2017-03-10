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
    #print(r)
    return r

def crawler(download):
    soup=BeautifulSoup(download)
    #print(soup)

    job=[]
    company=[]
    location=[]
    salary=[]
    require=[]
    information=[]

    #job_list=soup.find('ul',attrs={'class':'item_con_list'})
    #print(job_list)


    #sub_list=job_list.find_all('li')
    sub_list = soup.find_all('li')
    print(sub_list)

    for each_list in sub_list:
        print(each_list)
        jo=each_list.find('h2').text
        lo=each_list.find('em').text
        sa=each_list.find('span',attrs={'class':'money'}).text
        req=each_list.find('div',attrs={'class':'li_b_l'}).text.replace(' ','')
        co=each_list.find('div',attrs={'class':'company_name'}).find('a').text
        info=each_list.find('div',attrs={'class':'industry'}).text.replace(' ','')

        job.append(jo)
        location.append(lo)
        salary.append(sa)
        require.append(req)
        company.append(co)
        information.append(info)

    return job,location,salary,require,company,information


def main():
    url=furl
    download=download_url(url)
    resj,resl,ress,resr,resc,resi=crawler(download)
    if not os.path.exists('/home/xuyang/PycharmProjects/爬虫文件汇总'):
        os.mkdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    os.chdir('/home/xuyang/PycharmProjects/爬虫文件汇总')

    with codecs.open('拉钩python招聘信息.txt','wb',encoding='utf-8') as f:
        final=[[a,b,c,d,e,f,] for a,b,c,d,e,f in zip(resj,resl,ress,resr,resc,resi)]
        for i in final:
            f.write(i+'\n')

if __name__=='__main__':
    main()