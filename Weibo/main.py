from Weibo.crawler import WeiBoCrawler
import time
import requests

headers = {
    'authority': 'weibo.cn',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'ALF=1590252555; SCF=AuyBnr4HvZH7JQCybmP3ZH_XVlXr6iqelzsV4fUOTSjWn7c8h6LY526RZu3L5SsE3McwvO6lmb8-ddxAkFcrAXg.; SUB=_2A25zpbfGDeRhGeNH7VIZ8i7JyT6IHXVRadmOrDV6PUJbktAKLUHAkW1NSo5mARRmBB79AgUFZBvwuLgdPBg7w8HJ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnY-0qw8K7UDJ04PJPHz815JpX5K-hUgL.Fo-4So5Reo5feoz2dJLoI0qLxKBLB.zL122LxK-LBKBLBK.LxKBLBonL12BLxK-L1h2L1-2LxKBLB.2LB.2LxKBLB.2L1hqt; SUHB=0YhR8lMDIpcU89; SSOLoginState=1587660694; _T_WM=a0ed342bd98a23348c5c437a41579d98',
}

if __name__ == '__main__':

    c = WeiBoCrawler(headers=headers)
    wbs = c.get_all_weibo_by_userid(user_id="5225912372")

    for wb in wbs:
        print("weibo | ", wb.content)

# 1、拿到第一页微博，统计微博数量
# 2、每条微博的评论数，并自定义一种比较友好的方式保存到文件里面
# 3、统计谁评论的最多
# 4、保存第一微博的图片
# 5、统计转发微博多少，原创微博有多少
