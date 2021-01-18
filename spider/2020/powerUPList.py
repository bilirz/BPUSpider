#引入 · 引入所需要的库
import requests
from requests.adapters import HTTPAdapter
#输出 · 把爬取到的数据输出到这个路径
output_path = 'D:/BPU/BPUList.txt'
#URL · B站官方提供的BPU的json数据
url = 'https://www.bilibili.com/activity/web/view/data/814?csrf=bad828ceb3a088d054be3714732d0040'
#实例 · 创建会话实例
session = requests.session()
#实例 · 请求三次失败自动重连
session.mount('https://', HTTPAdapter(max_retries=3))
#获取 · 获取BPU的json数据
response = session.get(url)
#解析 · 对json进行解析
json_data = response.json()
#输出 · 输出获取的数据
with open(output_path, 'a', encoding="utf-8-sig") as f:
    #判断 · code等于0即可正常访问
    if json_data['code'] == 0:
        #循环 · 获得每一个BPU的uid
        for i in json_data['data']['list']:
            #保存 · 保存uid信息在row里
            row = '{}\n'.format(i['data']['uid'])
            #写入 · 写入row
            f.write(row)
    #判断 · code等于-412时
    elif json_data['code'] == -412:
        print('请求被拦截')
    else:
        #查看 · 打印爬到的是什么
        print(response)