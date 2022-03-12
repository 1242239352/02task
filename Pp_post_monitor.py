from urllib import parse
import requests
from time import sleep
import json
import urllib3
import datetime
class PPshoping:
    def __init__(self):
        self.url=""
        urllib3.disable_warnings()


    #访问请求
    def PP_collection(self,ShoppingName):
        #数据请求地址
        url = "https://j1.pupuapi.com/client/search/search_box/products?page=1&place_id=4424377b-5314-4e3e-a180-b3613be6804e&place_zip=350104&search_term="+ShoppingName+"&search_term_from=30&size=20&sort=0&store_id=8d3527f7-8c25-4e47-8a8d-ddd6dcde439b"
        #请求地址对应协议头
        headers={
            "sign": "a274aa8faac2cc26d1cb1b8b937d197e",
            "timestamp":  "1647085191304",
            "pp-version": "2021062503",
            "pp_storeid": "8d3527f7-8c25-4e47-8a8d-ddd6dcde439b",
            "pp-placeid": "4424377b-5314-4e3e-a180-b3613be6804e",
            "User-Agent": "Pupumall/3.5.6;Android/5.1.1;8cf36133df9ac81a7cba3a08db0fca5a",
            "pp-userid": "fbd6f044-53ff-4d78-be3f-3294608e8311",
            "pp-os": "10",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIiLCJhdWQiOiJodHRwczovL3VjLnB1cHVhcGkuY29tIiwiaXNfbm90X25vdmljZSI6IjEiLCJpc3MiOiJodHRwczovL3VjLnB1cHVhcGkuY29tIiwiZ2l2ZW5fbmFtZSI6Ikh1Z3MgfiIsImV4cCI6MTY0NzA5MjY4MCwidmVyc2lvbiI6IjIuMCIsImp0aSI6ImZiZDZmMDQ0LTUzZmYtNGQ3OC1iZTNmLTMyOTQ2MDhlODMxMSJ9.hwBXxciOEwhpg_eXqSrYeHxa4MIKCnBpR0tRV5DRHVA",
            "X-B3-TraceId": "d7b0ab80c36da790",
            "X-B3-SpanId": "8f70235fd631bf20",
            "Host": "j1.pupuapi.com",
            "Connection": "Keep-Alive",
        }
        #get方式请求数据
        response =requests.get(url=url,headers=headers,verify=False)
        #调用json数据分割方法 分别取出对应数据
        jsonshopping=json.loads(response.text)
        Pupu_Title, Pupu_spec, Pupu_price, Pupu_market_price, Pupu_sub_name= self.PP_POST_JSON(jsonshopping,0)
        print("-----------------------商品："+Pupu_Title+"-----------------------")
        print("规格："+Pupu_spec)
        print("价格："+str(Pupu_price))
        print("原价/折扣价："+str(Pupu_market_price)+"/"+str(Pupu_price))
        print("详细信息："+Pupu_Title+" "+Pupu_sub_name)
        print("--------------------监控不同商品的价格波动--------------------")
        i=0
        while(True):
            Pupu_Title, Pupu_spec, Pupu_price, Pupu_market_price, Pupu_sub_name = self.PP_POST_JSON(jsonshopping, i)
            print("当前时间为"+str(self.GetNowTime())+" ,"+Pupu_Title+":价格为"+str(Pupu_price))
            sleep(3)
            i=i+1
            if(i==19):
                i=0

    #json数据分割
    def PP_POST_JSON(self,jsonshopping,i):
        # 标题
        Pupu_Title = jsonshopping['data']['products'][i]['name']
        # 规格
        Pupu_spec = jsonshopping['data']['products'][i]['spec']
        # 折扣价格
        Pupu_price = round(jsonshopping['data']['products'][i]['price'] / 100, 1)
        # 原价
        Pupu_market_price = round(jsonshopping['data']['products'][i]['market_price'] / 100, 1)
        # 详细内容
        Pupu_sub_name = jsonshopping['data']['products'][i]['sub_title']
        return Pupu_Title,Pupu_spec,Pupu_price,Pupu_market_price,Pupu_sub_name
    
    #返回当前时间
    def GetNowTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def run(self):
        #url（utf-8）编码
        Search_goods=parse.quote("牛肉")
        self.PP_collection(Search_goods)

if __name__ == '__main__':
    PPshoping().run()
