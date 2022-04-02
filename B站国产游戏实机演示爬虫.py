import requests
import random
import csv
import time
import json

ua = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
"""
def get_data(aid):
    url = "http://api.bilibili.com/archive_stat/stat?aid="+str(aid)+"&type=jsonp"
    data = requests.get(url,headers={"user-agent":random.choice(ua)}).json()
    truedata = data['data']
    data_dict = {}
    data_dict["view"] = truedata["view"]
    data_dict["danmaku"] = truedata["danmaku"]
    data_dict["reply"] = truedata["reply"]
    data_dict["favorite"] = truedata["favorite"]
    data_dict["coin"] = truedata["coin"]
    data_dict["share"] = truedata["share"]
    data_dict["like"] = truedata["like"]
    return data_dict
    pass
"""
#获取推荐视频接口：http://api.bilibili.cn/author_recommend?aid=
#获取视频数据接口：http://api.bilibili.com/archive_stat/stat?aid=AV号&type=jsonp
#获取视频数据接口：https://api.bilibili.com/x/web-interface/view?bvid=BV号
#http://api.bilibili.com/x/web-interface/archive/stat?aid=
def bvtoav(bid):
    html = 'https://api.bilibili.com/x/web-interface/view?bvid='+bid
    data = requests.get(html,headers={"user-agent":random.choice(ua)}).json()
    truedata = data['data']
    aid = truedata['aid']
    time.sleep(0.1*random.randint(1,2))
    return aid

def avtobv(aid):
    html = 'http://api.bilibili.com/x/web-interface/archive/stat?aid='+str(aid)
    data = requests.get(html,headers={"user-agent":random.choice(ua)}).json()
    truedata = data['data']
    bid = truedata['bvid']
    time.sleep(0.1*random.randint(1,2))
    return bid

def get_videos(aid):
    videos_dict = {}
    url = "http://api.bilibili.cn/author_recommend?aid="+str(aid)
    res = requests.get(url,headers={"user-agent":random.choice(ua)})
    res.encoding = 'UTF-8'
    video_list = res.json()["list"]
    for items in video_list:
        video_name = items["title"]
        video_aid = items["aid"]
        videos_dict[video_name] = video_aid
    time.sleep(0.1*random.randint(1,2))
    return videos_dict
    pass


def save_to_csv(dict_):
    with open ('国产游戏实机演示数据.csv','w',encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        table_header = ["视频名","up主","播放","弹幕","回复","收藏","硬币","分享","点赞"]
        writer.writerow(table_header)
        for items in dict_:
            datalist = []
            print(items)
            items = json.loads((str(dict_[items]).replace("'",'"')), strict=False)
            datalist.append(items["videoname"])
            datalist.append(items["uper"])
            datalist.append(items["usefuldata"]["view"])
            datalist.append(items["usefuldata"]["danmaku"])
            datalist.append(items["usefuldata"]["reply"])
            datalist.append(items["usefuldata"]["favorite"])
            datalist.append(items["usefuldata"]["coin"])
            datalist.append(items["usefuldata"]["share"])
            datalist.append(items["usefuldata"]["like"])
            writer.writerow(datalist)
        pass
    pass

def get_data(bid):
    url = "https://api.bilibili.com/x/web-interface/view?bvid="+bid
    res = requests.get(url,headers={"user-agent":random.choice(ua)})
    res.encoding='UTF-8'
    data = res.json()["data"]
    video_data = {}
    video_data["videoname"] = data["title"]
    video_data["bid"] = data["bvid"]
    video_data["aid"] = data["aid"]
    video_data["uper"] = data["owner"]["name"]
    video_data["usefuldata"] = data["stat"]
    time.sleep(0.1*random.randint(1,2))
    return video_data
    pass

def main():
    start_bv_list = ['BV1AS4y1X7Ns','BV13i4y1Q7nt','BV15P4y1M7mQ']
    geted_av_list = []
    for items in start_bv_list:
        geted_av_list.append(str(bvtoav(items)))
    data_dict = {}
    keywords_list = ["实机","演示","宣传","预告"]
    for items in start_bv_list:
        data_dict[items] = get_data(items)
    print("初始数据获取成功")
    while len(geted_av_list) <= 200:
        for aids in geted_av_list:
            videos_dict = get_videos(aids)
            for keywords in keywords_list:
                for video_names in videos_dict:
                    if keywords in video_names:
                        geted_av_list.append(videos_dict[video_names])
                        video_bid = avtobv(videos_dict[video_names])
                        data_dict[video_bid] = get_data(video_bid)
                        print(len(data_dict))
                        if len(data_dict) >= 50:
                            break
                if len(data_dict) >= 50:
                    break
            if len(data_dict) >= 50:
                break
        if len(data_dict) >= 50:
            break
        pass
    #print(str(data_dict))
        #print(data_dict[videos])
    save_to_csv(data_dict)
    print("写入成功")

if __name__ == '__main__':

    main()