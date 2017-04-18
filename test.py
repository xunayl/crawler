#coding:utf-8

from bs4 import BeautifulSoup
import requests
import time
import codecs
import os
import json

url='https://www.zhihu.com'
loginURL='https://www.zhihu.com/login/email'
headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "https://www.zhihu.com/",
        'Host': 'www.zhihu.com',
             }

c = []
with codecs.open('password', 'rb', encoding='utf-8') as f:
    for i in range(2):
        i = f.readline()
        c.append(i)

data={'email': str(c[0]).replace('\n', ''),
        'password': str(c[1]),
        'rememberme': "true",}

def login():

    global s
    s=requests.session()
    global xsrf

    req = s.get(url, headers=headers)
    print('1:')
    print(s.cookies)
    soup = BeautifulSoup(req.text, "html.parser")
    xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')

    if os.path.exists('cookiefile.txt'):
        with codecs.open('cookiefile.txt') as f:
            cookie=json.load(f)
        s.cookies.update(cookie)

    else:

        data['_xsrf'] = str(xsrf)
        headers['X-Xsrftoken'] = str(xsrf)
        t = str(int(time.time() * 1000))
        captchaURL = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        print(captchaURL)
        with open('zhihucaptcha.gif', 'wb') as f:
            captchaREQ = s.get(captchaURL, headers=headers)
            f.write(captchaREQ.content)
        loginCaptcha = input('input captcha:\n').strip()
        data['captcha'] = loginCaptcha
        s.post(loginURL, headers=headers, data=data)
        print('2:')
        print(s.cookies)
        with codecs.open('cookiefile.txt','w') as f:
            json.dump(s.cookies.get_dict(),f)

def nextpage():
    req_rel=s.get(url,headers=headers)
    print(s.cookies)
    print(data)
    print(headers)
    print()
    print('哈哈哈哈哈哈')
    print()
    headers['X-Xsrftoken']=xsrf
    headers['X-Requested-With']='XMLHttpRequest'
    postdata={'params':'{"offset":30,"start":"19"}','method':'next'}
    req_nextpage=s.post(url='https://www.zhihu.com/node/TopStory2FeedList',headers=headers,data=postdata)
    print(req_nextpage)
    print(req_nextpage.text)

login()
nextpage()