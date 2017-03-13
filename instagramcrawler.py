

from bs4 import BeautifulSoup
import os
import codecs
import requests
import json

url='https://www.instagram.com/graphql/query/?query_id=17861995474116400&fetch_media_item_count=12&fetch_media_item_cursor=KKcBARAAAAIoABgAEAAIAAgACAAIAP___-9__-_____--7____7___________7__vf_____f___7-_v__7____f_v__3r____v_53fv______8_-__D63-c4HPkrf-DvH79__3__v3_99-__3_u9v3__X9vv___x__9__f_rf__x_t____r_H33___8__2_-f__-_9_-9_3__f-_f1_9-0-75EM4hpAMRAW6OrP6thWAA%3D%3D&fetch_comment_count=4&fetch_like=10'
headers={'Cookie':'mid=WMY8ngAEAAHJwO6cDUr4k9Wyggrx; sessionid=IGSCb3396983624006efaa740e5f746e1b48653af125498a212b9f89884940e35f49%3AaVgZzOKPQeRFjjVNeu86oUZg5odlZFOT%3A%7B%22_auth_user_id%22%3A1441480119%2C%22_auth_user_hash%22%3A%22%22%2C%22asns%22%3A%7B%22time%22%3A1489386762%2C%2258.210.212.110%22%3A4134%7D%2C%22last_refreshed%22%3A1489386761.7133288383%2C%22_token%22%3A%221441480119%3AB3Em33b5ZMff4d3BUNAuwFMnKzk0CKAc%3A4212625d592df8f583931562225563a01deecd6d739ef4e756448a1addbd4fde%22%2C%22_platform%22%3A4%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_token_ver%22%3A2%7D; s_network=""; csrftoken=30zkIjd1Tvf95jNyxSDWFdGPh9lsg6aO; ds_user_id=1441480119; ig_pr=1; ig_vw=472','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}


def download_page(url):
    r=requests.get(url,headers=headers).text
    #print(type(r))#变成字符串
    #print(r)
    return r

def crawler(download):
    img=json.loads(download)
    result=[]
    #print(type(img))#变成字典
    for i in range(12):
        pic = img.get('data').get('user').get('edge_web_feed_timeline').get('edges')[i].get('node').get('display_url')
        result.append(pic)
    return result

def main():
    if not os.path.exists('/home/xuyang/PycharmProjects/爬虫文件汇总/instagram'):
        os.mkdir('/home/xuyang/PycharmProjects/爬虫文件汇总/instagram')
    os.chdir('/home/xuyang/PycharmProjects/爬虫文件汇总/instagram')

    download=download_page(url)
    res=crawler(download)
    final=requests.get(res[0],headers=headers)
    with codecs.open('0', 'wb') as f:
        f.write(final.content)



if __name__ == '__main__':
    main()
