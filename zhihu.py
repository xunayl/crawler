from selenium import webdriver
import codecs
import time
from bs4 import BeautifulSoup

def crawler():
    # 以下为登录知乎流程

    # 知乎url
    url = 'https://www.zhihu.com/'

    # 打开chrome
    driver = webdriver.Chrome()

    # 打开知乎
    driver.get(url)
    time.sleep(2)

    # 从写好的文本中提取账号密码
    # 我写的格式为第一行账号，第二行密码
    c = []
    with codecs.open('password', 'rb', encoding='utf-8') as f:
        for i in range(2):
            i = f.readline()
            c.append(i)

    # 以下两句相同 点击跳到登录
    # driver.find_element_by_link_text('登录').click()
    driver.find_element_by_xpath("//*[contains(text(),'登录')]").click()

    # 输入账号密码
    driver.find_element('name', 'account').send_keys(str(c[0]).replace('\n', ''))
    time.sleep(2)
    driver.find_element('name', 'password').send_keys(str(c[1]))
    time.sleep(2)

    # 以下两句为点击登录按钮
    # driver.find_element_by_xpath("//button[@class='sign-button submit']").click()
    driver.find_element_by_xpath("//button[contains(text(),'登录')]").click()
    time.sleep(2)

    # 定义一个实现将滚轮滑到页面最下方的功能的函数
    def execute_times(times):
        for i in range(times):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(3)

    # 可自定义翻页次数
    execute_times(5)

    # 取得页面的源码
    # print(driver.page_source)
    html = driver.page_source

    # 使用beautifulsoup处理
    soup = BeautifulSoup(html, 'lxml')

    # 定义用来存储信息的列表
    ques = []
    qlink = []
    name = []
    addr = []
    intro = []

    # select使用了beautifulsoup的css选择器
    # 相关教程：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

    # 找到问题名和对应链接所在
    hostques = soup.select('a.question_link')

    # 找到首页上热门回答者的昵称和主页链接所在
    authors = soup.select('a.author-link')
    # print(authors)

    # 找到回答者的个性签名
    authors_intro = soup.select('span.bio')

    # 提取问题名和问题链接
    for each_ques in hostques:
        ques.append(each_ques.text)
        qlink.append('http://www.zhihu.com' + each_ques['href'])

    # 提取昵称和个人主页至存储信息的列表中
    for each_author in authors:
        name.append(each_author.text)
        addr.append('http://www.zhihu.com' + each_author['href'])
    # print(name)
    # print(each_author['href'])

    # 提取个人签名
    for each_intro in authors_intro:
        intro.append(each_intro['title'])
    # print(each_intro.text)

    with codecs.open('知乎首页热门答主信息.txt', 'wb', encoding='utf-8') as f:
        for ques_title, ques_link, author_name, author_link, author_intro in zip(ques, qlink, name, addr, intro):
            f.write('问题：%s\n问题链接：%s\n答主昵称：%s\n主页：%s\n个性签名：%s\n\n' % (
            ques_title.replace('\n', ''), ques_link, author_name, author_link, author_intro))

    driver.quit()


def main():
    crawler()

if __name__ == '__main__':
    main()