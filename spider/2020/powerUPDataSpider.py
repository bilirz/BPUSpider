#引入 · 引入所需要的库
import requests
import time
import sys
import csv
import time
from requests.adapters import HTTPAdapter
#输出 · 把爬取到的数据输出到这个路径
output_path = "D:/BPU/BPUData.csv"
#打开 · 打开需要爬取的UP主uid并以换行符分割成列表
uids = open('D:/BPU/BPUList.txt', encoding='utf-8-sig').read().split('\n')
#处理 · 去掉列表中所有的所有空值
uid_list = [u for u in uids if u != '']
#打开 · 打开headers文件并以换行符分割成列表
hearers_list = open('D:/BPU/headers.txt', encoding='utf-8-sig').read().split('\n')
headers = {
    "User-Agent": hearers_list[0],
    "Cookie": hearers_list[1]
}
#URL · B站官方提供的BPU的json数据
card_url = 'http://api.bilibili.com/x/web-interface/card?mid={}'
upstat_url = 'http://api.bilibili.com/x/space/upstat?mid={}'
#实例 · 创建会话实例
session = requests.session()
#实例 · 请求三次失败自动重连
session.mount('https://', HTTPAdapter(max_retries=3))

with open(output_path, 'a', encoding="utf-8-sig", newline='') as f:
    csv_headers = ['mid','name','fans','archive','article','likes','time']
    f_csv = csv.writer(f)
    f_csv.writerow(csv_headers)
    for u in uid_list:
        card = session.get(card_url.format(u),headers = headers).json()
        upstat = session.get(upstat_url.format(u),headers = headers).json()
        if card['code'] == 0 | upstat['code'] == 0:
            #保存 · 保存uid信息在row里
            row = [card['data']['card']['mid'],card['data']['card']['name'],card['data']['card']['fans'],upstat['data']['archive']['view'],upstat['data']['article']['view'],upstat['data']['likes'],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
            #写入 · 写入row
            f_csv.writerow(row)
        #判断 · code等于-412时
        elif card['code'] == -412 or upstat['code'] == -412:
            print('请求被拦截')
        elif card['code'] == -400 or upstat['code'] == -400:
            print(uids)
        else:
            #查看 · 打印爬到的是什么
            print(str(card)+str(upstat))
        #缓冲 · 给服务器点时间——
        time.sleep(10)