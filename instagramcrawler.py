from bs4 import BeautifulSoup
import time
import codecs
from selenium import webdriver

url='https://www.instagram.com/'

#def download_page(url):
    #pass


#def crawler():
    #pass

#def main():
    #download_page(url)

#if __name__ == '__main__':
    #main()
res=[]
with codecs.open('password','rb',encoding='utf-8') as f:
    for i in range(2):
        res.append(f.readline())
driver=webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.find_element_by_link_text('请登录').click()
driver.find_element_by_name('username').send_keys(str(res[0]).replace('\n',''))
driver.find_element_by_name('password').send_keys(str(res[1]))
driver.find_element_by_xpath("//button[contains(text(),'登录')]").click()
#####此处完成到可以登录
