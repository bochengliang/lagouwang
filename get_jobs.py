import requests
import os
import math
import time
import json
import pymysql
total_data = []
def createfile(): #创建文件夹
    try:
        os.makedirs('D:/employment')
    except:
        pass

def get_json_data(page,city,job):
    url ='https://www.lagou.com/jobs/positionAjax.json' #深圳
    data = {
        'city': city,
        'needAddtionalResult': 'false',
        'first':'true',
        'pn':page,
        'kd':job
    }
    headers = {
        'Referer':'https://www.lagou.com/jobs/list_?px=default&city=%E4%B8%8A%E6%B5%B7',#一定要加
        'Cookie':'_ga=GA1.2.1182018860.1542626889; user_trace_token=20181119192805-2ed58121-ebee-11e8-a733-525400f775ce; LGUID=20181119192805-2ed5841f-ebee-11e8-a733-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167343074cd313-03ee6ba948a4d-4313362-921600-167343074ce492%22%2C%22%24device_id%22%3A%22167343074cd313-03ee6ba948a4d-4313362-921600-167343074ce492%22%7D; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=3; JSESSIONID=ABAAABAAAGFABEF81DB7EAD709820C3449430A54841C116; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542626889,1542675355,1542675367,1542871929; X_HTTP_TOKEN=8612e6124962a459760c05c00fb7c5d1; index_location_city=%E5%85%A8%E5%9B%BD; LG_LOGIN_USER_ID=2044767b9f7af7dbdbee71b1e493098b9ad63a3b0386a1cd8c0425d9c6b2f8dd; _putrc=3D90BAE753975BF7123F89F2B170EADC; login=true; unick=%E6%A2%81%E6%88%90%E6%B3%A2; TG-TRACK-CODE=search_code; LGSID=20181123174431-60cd8722-ef04-11e8-b6dc-525400f775ce; _gat=1; gate_login_token=c18434a729bd643de4f941b632ff384a1acff8d4d3096213d763f61c1b4fd236; SEARCH_ID=8a389493a3ef42059425c20cc32b988d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542968596; LGRID=20181123182314-c9771c00-ef09-11e8-8afd-5254005c3644',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequestIONID=ABAAABAAAGGABCB7C6E5C5C79DB36D456E2AE5713DCC959; _ga=GA1.2.1182018860.1542626889; user_trace_token=20181119192805-2ed58121-ebee-11e8-a733-525400f775ce; LGUID=20181119192805-2ed5841f-ebee-11e8-a733-525400f775ce; X_HTTP_TOKEN=8612e6124962a459760c05c00fb7c5d1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542626889,1542675355,1542675367; LGSID=20181121105402-b3a0cf3a-ed38-11e8-8a7a-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fxiaoyuan.lagou.com%2F; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167343074cd313-03ee6ba948a4d-4313362-921600-167343074ce492%22%2C%22%24device_id%22%3A%22167343074cd313-03ee6ba948a4d-4313362-921600-167343074ce492%22%7D; sajssdk_2015_cross_new_user=1; _putrc=3D90BAE753975BF7123F89F2B170EADC; login=true; unick=%E6%A2%81%E6%88%90%E6%B3%A2; _gat=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=3; gate_login_token=7af59fb1e9e4b401f4aa3d9df1eea45c59a994523eb383690187054b5d042f0a; index_location_city=%E5%85%A8%E5%9B%BD; LGRID=20181121110117-b722d7b4-ed39-11e8-8a7a-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542769280; TG-TRACK-CODE=index_navigation',
    }
    response = requests.post(url,headers=headers,data=data)
    Data = response.json()
    return Data
def get_my_city():
    city_list = []
    with open('D:city/city.txt', 'r') as f:
        for line in f:
            city_list.append(line.strip())
    return city_list
def connect_mysql():
    db = pymysql.connect("localhost", "root", "1997", "ip", charset='utf8')
    cursor = db.cursor()

def get_page_num(Count):
    count = math.ceil(Count/15)
    if count > 30:
        count = 30
    else:
        count = count
    return count
def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    cities = get_my_city()
    jobs = ['python','java','Ruby','Node.js','C++','HTML5','Android','Shell','Go','JavaScript','C','C#','Hadoop']
    for city in cities:
        for job in jobs:
            try:
                print("-------------------------------------------{}的{}职位爬取开始！-----------------------------".format(city,job))
                Page_1 = get_json_data('1',city,job)
                Total_Count = Page_1['content']['positionResult']['totalCount'] #得到总职位数
                num = get_page_num(Total_Count)
                print('职位总数:{},页数:{}'.format(Total_Count, num))
                for j in range(1,num+1):
                    page_json = get_json_data(str(j),city,job)
                    print("---------------------------蜘蛛正在爬取第{}页-------------------------------".format(str(j)))
                    data_page_json = page_json['content']['positionResult']['result']
                    for d in data_page_json:
                        print(d)
                        with open('D:/employment/rexg.json','a',encoding='utf-8') as f:
                            json_str = json.dumps(d, ensure_ascii=False)  # 一条数据
                            f.write(json_str)
                            f.write('\n')
                    time.sleep(1)
            except:
                print("------------------------------出现异常-----------------------")

if __name__ == '__main__':
    main()
