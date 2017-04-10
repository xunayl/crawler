import re
import requests
import csv
from bs4 import BeautifulSoup
import time
import codecs
url6001000='http://bj.58.com/pinpaigongyu/?minprice=600_1000&PGTID=0d3111f6-0000-1852-505b-f8120a4c4080&ClickID=1'
url10001500='http://bj.58.com/pinpaigongyu/?minprice=1000_1500&PGTID=0d3111f6-0000-1cae-2424-c03b5cb85ba5&ClickID=1'
url15002000='http://bj.58.com/pinpaigongyu/?minprice=1500_2000&PGTID=0d3111f6-0000-1e38-ed89-211d1f8f07df&ClickID=1'
url20003000='http://bj.58.com/pinpaigongyu/?minprice=2000_3000&PGTID=0d3111f6-0000-14d0-54eb-3f390b8ff863&ClickID=1'
url30005000='http://bj.58.com/pinpaigongyu/?minprice=3000_5000&PGTID=0d3111f6-0000-1726-77aa-83bff2e067a4&ClickID=1'
url50008000='http://bj.58.com/pinpaigongyu/?minprice=5000_8000&PGTID=0d3111f6-0000-1db6-ddbb-4bbbed9f1dfd&ClickID=1'
url8000='http://bj.58.com/pinpaigongyu/?minprice=8000_30000&PGTID=0d3111f6-0000-10a7-608d-a84eea28d94c&ClickID=1'

urlhead='http://bj.58.com'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

numb=input('请输入你想选择的价格区间:\n1代表价格区间为600-1000\n2代表价格区间为1000-1500\n3代表价格区间为1500-2000\n4代表价格区间为2000-3000\n5代表价格区间为3000-5000\n6代表价格区间为5000-8000\n7代表价格区间为8000以上\n')
if numb=='1':
    url=url6001000
elif numb=='2':
    url=url10001500
elif numb=='3':
    url=url15002000
elif numb=='4':
    url=url20003000
elif numb=='5':
    url=url30005000
elif numb=='6':
    url=url50008000
elif numb=='7':
    url=url8000
else:
    print('输入不合法')
    exit()

house_link = []
house_money = []
house_location = []
house_title=[]
while url:
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')
    if soup.find('ul', attrs={'class': 'list'})and soup.find('a', attrs={'class': 'next'}):
        house_list = soup.find('ul', attrs={'class': 'list'}).find_all('li')
        t = re.compile(r'<h2>(.*)</h2>')
        house_title += re.findall(t, r)
        for i in house_list:
            house_link.append(urlhead + i.find('a')['href'])
            house_money.append(i.select('.money')[0].select('b')[0].text + '元/月')
        for i in house_title:
            house_location.append(i.split()[1])

        url = urlhead + soup.find('a', attrs={'class': 'next'})['href']
    else:
        url = None

with codecs.open('renttest.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for a, b, c, d in zip(house_title, house_money, house_location, house_link):
        csv_writer.writerow([a, b, c, d])

