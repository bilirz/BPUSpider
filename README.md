# 哔哩哔哩百大UP主爬虫
这是一个可以爬取哔哩哔哩百大UP主(BPU)的爬虫。

**使用的库**

使用了`requests`库，这是一个基于`urllib`编写的HTTP客户端库，简单易用。

因为是第三方库,所以使用前需要`cmd`安装

`pip install requests`

## 如何使用本项目

制作hearers.txt

```
User-Agent
Cookie(只需要SESSDATA部分即可)
```

如果成功配置了环境，并且安装好了所需的库：

```bash
cd spider
cd 2020
python run.py
```

## LICENSE

MIT [©bilirz](https://github.com/bilirz)
