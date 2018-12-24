import requests
from bs4 import BeautifulSoup
import os
def get_all_jobs():
    headers = {
        'Host': 'www.lagou.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    jobs = []
    category = []
    url = 'https://www.lagou.com/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    lis = soup.find_all('div','category-list')
    for i in lis:
        td = i.find_all('h2')
        for j in td:
            category.append(j.string.strip())
        td1 = i.find_all('a')
        for j1 in td1:
            jobs.append(j1.string)
def get_all_citys():
    headers = {
        'Host': 'www.lagou.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    data = {
        'keyword': 'java',
        'px': 'default',
        'city': '北京',
        'positionNum': '500' ,
        'companyNum': '0',
        'isCompanySelected': 'false',
        'labelWords':''
    }
    city = []
    url = 'https://www.lagou.com/jobs/allCity.html'
    response = requests.get(url,headers=headers,params=data)
    # print(response.text)
    soup = BeautifulSoup(response.text,'lxml')
    lis = soup.find_all('ul','city_list')
    for i in lis:
        td = i.find_all('a')
        for j in td:
            city.append(j.string)
    try:
        os.makedirs('D:city')
    except:
        pass
    with open('D:city/city.txt','w') as f:
        for i in city:
            f.write(i+'\n')
def get_my_city():
    city_list = []
    with open('D:city/city.txt', 'r') as f:
        for line in f:
            city_list.append(line.strip())
    return city_list





