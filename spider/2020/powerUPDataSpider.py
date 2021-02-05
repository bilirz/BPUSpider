# 引入 · 引入所需要的库
import requests
import time
import sys
import csv
from requests.adapters import HTTPAdapter

# 输出 · 把爬取到的数据输出到这个路径
output_path = "D:/BPU/BPUData.csv"
# 打开 · 打开需要爬取的UP主uid并以换行符分割成列表
with open("D:/BPU/BPUList.txt", "r", encoding="utf-8-sig") as f:
    uids = f.read().split("\n")
# 处理 · 去掉列表中所有的所有空值
uid_list = [u for u in uids if u != ""]
# 配置 · 在此处配置User-Agent和Cookie(只需要SESSDATA部分即可)
headers = {"User-Agent": "", "Cookie": ""}
# URL · B站官方提供的BPU的json数据
card_url = "http://api.bilibili.com/x/web-interface/card?mid={}"
upstat_url = "http://api.bilibili.com/x/space/upstat?mid={}"
# 实例 · 创建会话实例
session = requests.session()
# 实例 · 请求三次失败自动重连
session.mount("https://", HTTPAdapter(max_retries=3))

with open(output_path, "a", encoding="utf-8-sig", newline="") as f:
    # 保存 · 设置表头
    csv_headers = ["mid", "name", "fans", "archive", "article", "likes", "time"]
    f_csv = csv.writer(f)
    f_csv.writerow(csv_headers)
    for u in uid_list:
        card = session.get(card_url.format(u), headers=headers).json()
        upstat = session.get(upstat_url.format(u), headers=headers).json()
        if card["code"] == 0 | upstat["code"] == 0:
            # 保存 · 保存uid信息在row里
            row = [
                card["data"]["card"]["mid"],
                card["data"]["card"]["name"],
                card["data"]["card"]["fans"],
                upstat["data"]["archive"]["view"],
                upstat["data"]["article"]["view"],
                upstat["data"]["likes"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            ]
            # 写入 · 写入row
            f_csv.writerow(row)
        # 判断 · 当code等于-412 -400或-404时
        elif card["code"] == -412 or upstat["code"] == -412:
            print("请求被拦截")
            sys.exit()
        elif card["code"] == -400 or upstat["code"] == -400:
            print("请求错误")
        elif card["code"] == -404 or upstat["code"] == -404:
            print("用户不存在")
        else:
            # 查看 · 打印爬到的是什么
            print(str(card) + str(upstat))
        # 缓冲 · 给服务器点时间——
        time.sleep(5)
