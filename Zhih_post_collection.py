import requests
from time import sleep
import json
import urllib3
import re
import os
class ZhihuPost:

    def __init__(self):
        self.url=""
        #收藏夹名称数组
        self.FavoritesTitle=[]
        #收藏夹名称类型对应的访问id数组
        self.FavoritesId=[]
        urllib3.disable_warnings()

    #知乎收藏夹数据采集
    def Zhihu_Favorites_collection(self):
        #知乎主页地址
        url="https://www.zhihu.com/people/13559453225/collections"
        headers = {
            "Host": "www.zhihu.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "sec-ch-ua-mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://www.zhihu.com/search?type=content&q=%E6%96%87%E5%AD%A6",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        # get方式请求数据
        response = requests.get(url=url, headers=headers, verify=False)
        self.FavoritesId,self.FavoritesTitle=self.Re_Favorites_IdAndTitle(response.text)
        for i in range(len(self.FavoritesId)):
            self.Zhihu_Subclass_collection(self.FavoritesId[i],self.FavoritesTitle[i])
            sleep(3)

    #知乎收藏夹子类数据采集
    def Zhihu_Subclass_collection(self,urlid,title):
        # 知乎主页地址
        url = "https://www.zhihu.com/api/v4/collections/"+urlid+"/items?offset=0&limit=20"
        print(url)
        headers = {
            "Host": "www.zhihu.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "x-zse-93":"101_3_2.0",
            "sec-ch-ua-mobile": "0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "x-requested-with":"fetch",
            "x-zse-96":"2.0_aTx0e498rTFpU920ThS8cQe8UGYf2_S0zCNBQ4U0gGFX",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.zhihu.com/collection/"+urlid,
            "Accept-Language": "zh-CN,zh;q=0.9",
        }
        # get方式请求数据
        response = requests.get(url=url, headers=headers, verify=False)
        # loads方法是把json对象转化为python对象
        jsonzhihu= json.loads(response.text)
        # 调用json数据分割方法 分别取出对应数据
        self.Zhihu_json(jsonzhihu,title)

    #正则取收藏夹的标题 及对应收藏夹链接ID 返回匹配到的数据的数组
    def Re_Favorites_IdAndTitle(self,Text):
       #str_1="<a href='/collection/789393912' rel='noreferrer noopener'>文学</a><a href='/collection/789393111912' rel='noreferrer noopener'>文学111</a><a href='/collection/789393922212' rel='noreferrer noopener'>文学2222</a>"
        FavoritesTitle=[]
        FavoritesId=re.findall(r"<a class=\"SelfCollectionItem-title\" href=\"/collection/(.*?)\" rel",Text)
        for i in FavoritesId:
            str=re.findall(r"<a class=\"SelfCollectionItem-title\" href=\"/collection/"+i+"\" rel=\"noreferrer noopener\">(.*?)</a>",Text)
            FavoritesTitle.append(str[0])
        return FavoritesId,FavoritesTitle

    #解析json数据 取出相关内容 并写入文档中
    def Zhihu_json(self,JsonText,sctitle):
        # 取出对象数
        num = JsonText['paging']['totals']
        print("对象数="+str(num))
        for i in range(0,num-1,1):
            try:
                # 标题
                title = JsonText['data'][i]['content']['question']['title']
                # 链接
                scurl = JsonText['data'][i]['content']['question']['url']
                # 部分内容
                BfText = JsonText['data'][i]['content']['excerpt']
            except Exception:
                # 标题
                title = JsonText['data'][i]['content']['title']
                # 链接
                scurl = JsonText['data'][i]['content']['url']
                # 部分内容
                BfText = JsonText['data'][i]['content']['excerpt_title']

            # 判断目录，有则打开，没有新建
            if os.path.exists(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容'):
                os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容')
            else:
                os.mkdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容')
                os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容')

            if os.path.exists(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容\\' + sctitle):
                os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容\\' + sctitle)
            else:
                os.mkdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容\\' + sctitle)
                os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容\\' + sctitle)

            # 往对应文件夹里添加内容
            Mlurl = r'C:\Users\ASUS\Desktop\构建之法作业\02\知乎收藏夹内容\\' + sctitle + '\\' + title + '.txt'
            myfile = open(Mlurl, 'w', encoding='utf-8')
            myfile.write(scurl + "\n" + BfText)
            myfile.close()
            print(sctitle+"收藏夹第"+str(i)+"篇文章"+title+"=》"+scurl+"=》爬取成功")
        print(title,scurl,BfText)
     #启动项
    def run(self):
        self.Zhihu_Favorites_collection()

if __name__ == '__main__':
    ZhihuPost().run()
