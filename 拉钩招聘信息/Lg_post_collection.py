import requests
from time import sleep
import json
from urllib import parse
import urllib3
import os
import xlwt
import time
class LaGouPost:

    def __init__(self):
        self.url=""
        #查询总职位数
        self.Cxnum=0
        #当前查询到哪个职位上数
        self.Dqnum=0
        self.positionName = []
        self.City = []
        self.District = []
        self.CompanyFullName = []
        self.CompanySize = []
        self.salary = []
        urllib3.disable_warnings()

    """
    拉钩招聘数据采集
    @:param Search_position 岗位
    @:param Pn 页数
    """
    def Lagou_collection(self,Search_position,Pn):
        #拉钩招聘数据api
        url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
        headers = {
            "Host": "www.lagou.com",
            "Connection": "keep-alive",
            "x-anit-forge-code": "0",
            "traceparent": "00-0e38f526c88a015f9d4ee1b728d6def7-c5a72bc5a4e47227-01",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accep": "application/json, text/javascript, */*; q=0.01",
            "x-requested-with": "XMLHttpRequest",
            "x-anit-forge-toke": "None",
            "Origin":"https://www.lagou.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.lagou.com/jobs/list_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "user_trace_token=20220313125217-3959f425-8090-4f14-9d21-eea79cafb1cc; _ga=GA1.2.589612377.1647147171; LGSID=20220313125252-9c7b70d7-2b04-4efc-895b-0a484f335d6f; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; LGUID=20220313125252-5264a6e2-29c8-4e57-af3b-68bd222be1c5; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1647147171; _gid=GA1.2.31684987.1647147247; sajssdk_2015_cross_new_user=1; gate_login_token=ad34d65330dcc2aa20fbc29795a01eb8cd8be27a97ee0334c6ecf65c0cb0105a; LG_LOGIN_USER_ID=aaa6d8fb24fb5f8475664272c2560a720b0af8677616f87778b3a0cbb05411fd; LG_HAS_LOGIN=1; _putrc=FAEB8F0633231DC8123F89F2B170EADC; JSESSIONID=ABAAAECABIEACCA9FB41C5C123C62AEEDA94168551121B6; login=true; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20220313%E4%B8%8B%E5%8D%8812:55:05125505-17f81a14971480-0035520476d2-2363163-2073600-17f81a14972bd2; sensorsdata2015session=%7B%7D; unick=%E6%96%B9%E6%99%93%E4%BD%B3; RECOMMEND_TIP=true; __SAFETY_CLOSE_TIME__18626316=1; index_location_city=%E5%85%A8%E5%9B%BD; __lg_stoken__=dbfefc871edf710df7582985dee2ffd8170c1e12dd6b7926f1b854fae0f914202be16c09469620d5b8751ffde1ba364e0e6df63c2e7098b6d247b87a4d9abf7000d7ed6ba8c6; TG-TRACK-CODE=search_code; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218626316%22%2C%22%24device_id%22%3A%2217f81a0646d68-09932428721ebe-2363163-2073600-17f81a0646e9c1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2290.0.4430.212%22%7D%2C%22first_id%22%3A%2217f81a0646d68-09932428721ebe-2363163-2073600-17f81a0646e9c1%22%7D; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1647148693; LGRID=20220313131815-bae5231f-a343-4ab6-a3e5-dbe187c7dbff; SEARCH_ID=c45f725c652a4a5b9c5ffbfeb91f0fe9; X_HTTP_TOKEN=038591d682f2abfb8888417461828b7bf478e167c2"
        }
        #post数据 岗位需要进行url utf-8编码
        data="first=true&pn="+str(Pn)+"&kd="+parse.quote(Search_position)
        #post方式请求数据
        response = requests.post(url=url,data=data ,headers=headers, verify=False)
        print(response.text)
        # loads方法是把json对象转化为python对象
        jsonLagou= json.loads(response.text)
        # 调用json数据分割方法 分别取出对应数据
        self.Lagou_json(jsonLagou)

    """
    解析json数据 取出相关内容 并写入文档中
    @:param JsonText json数据
    """
    def Lagou_json(self,JsonText):
        # 取出对象数
        num = JsonText['content']['positionResult']['resultSize']
        print("对象数="+str(num))

        for i in range(0,num-1,1):
            # 职位名称
            self.positionName.append(JsonText['content']['positionResult']['result'][i]['positionName'])
            # 市
            self. City.append(JsonText['content']['positionResult']['result'][i]['city'])
            # 区
            self.District.append(JsonText['content']['positionResult']['result'][i]['district'])
            # 公司名称
            self.CompanyFullName.append(JsonText['content']['positionResult']['result'][i]['companyFullName'])
            # 规模
            self.CompanySize.append(JsonText['content']['positionResult']['result'][i]['companySize'])
            # 薪资
            self.salary.append(JsonText['content']['positionResult']['result'][i]['salary'])
        print(self.positionName)
        print(self.City)
        print(self.District)
        print(self.CompanyFullName)
        print(self.CompanySize)
        print(self.salary)
        # 判断目录，有则打开，没有新建
        if os.path.exists(r'C:\Users\ASUS\Desktop\构建之法作业\02\拉钩招聘信息'):
            os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\拉钩招聘信息')
        else:
            os.mkdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\拉钩招聘信息')
            os.chdir(r'C:\Users\ASUS\Desktop\构建之法作业\02\拉钩招聘信息')

        print(self.Cxnum,self.Dqnum)
        if(self.Cxnum==self.Dqnum):
            # 保存数据到excel文件中
            self.sava_excel(self.positionName, self.City, self.District, self.CompanyFullName, self.CompanySize, self.salary)


    """
    保存数据到excel文件中
    @:param num             对象数量
    @:param positionName    职位名称
    @:param City            市
    @:param District        区
    @:param CompanyFullName 公司名称
    @:param CompanySize     规模
    @:param salary          薪资
    """
    def sava_excel(self,positionName,City,District,CompanyFullName,CompanySize,salary):
        #总数
        num=len(positionName)
        # 打开excel文件
        data = xlwt.Workbook()
        # 获取其中的一个sheet
        table = data.add_sheet('made')
        row=0 #行
        col=0 #列
        for i in range(0,num-1,1):
            table.write(row,col,  positionName[i])
            table.write(row, col+1, City[i])
            table.write(row, col+2, District[i])
            table.write(row, col+3, CompanyFullName[i])
            table.write(row, col+4, CompanySize[i])
            table.write(row, col+5, salary[i])
            row=row+1
            col=0
        data.save(r"C:\Users\ASUS\Desktop\构建之法作业\02\拉钩招聘信息\Lgtemp.xls")
        print("数据写入成功。")



     #启动项
    def run(self):
        str =['前端开发','java','Python','PHP']
        #查询岗位数
        self.Cxnum=len(str)
        for i in str:
            self.Dqnum = self.Dqnum+1
            self.Lagou_collection(i,self.Dqnum)


if __name__ == '__main__':
    LaGouPost().run()
