import json
import matplotlib.pyplot as plt
import re
from pyecharts import Geo
from pyecharts import Map
import pymysql
from collections import Counter
import jieba as jb
from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib
def set_china():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.unicode_minus'] = False
def get_json_data():
    res = []
    with open('D:/employment/totaldata.json', 'r', encoding='utf-8') as f:
        for line in f:
            json_str = json.loads(line)
            res.append(json_str)
    return res
def pie_chart():
    # plt.title('大编程语言在北上广深应用比例图')
    data = get_json_data()
    lan_list = []
    for d in data:
        try:
            res = re.search('[A-Za-z][A-Za-z]*', d['positionName'])
            lan_list.append(res.group().lower())
        except:
            continue
    result = Counter(lan_list).most_common(5)
    fracs = [result[0][1], result[1][1], result[2][1],result[3][1],result[4][1]]
    jobs = [result[0][0], result[1][0], result[2][0],result[3][0],result[4][0]]
    plt.axes(aspect=1)
    plt.pie(x=fracs, labels=jobs, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.show()
def education_chart(): #教育直方图
    pass
def wordl_cloud():
    s= []
    data = get_json_data()
    for item in data:
        if len(item['skillLables']) >=1:
            s +=item['skillLables']
    c = Counter(s)
    common_c = c.most_common(100)
    bg_pic = imread('D:/picture.jpg')
    wc = WordCloud(
        # 设置字体
        font_path='D:/chna.ttf',
        # 设置背景色
        background_color='white',
        # 允许最大词汇
        max_words=20,
        # 词云形状
        mask=bg_pic,
        # 最大号字体
        max_font_size=150
    )
    # 生成词云
    wc.generate_from_frequencies(dict(common_c))
    wc.to_file('skileswordcloud.png')
    # 生成图片并显示
    plt.figure()
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def city_job():
    num = []
    db = pymysql.connect("localhost", "root", "1997", "lagouwang", charset='utf8')
    cursor = db.cursor()
    sql1 = "select  COUNT(*) from cities_job where  city='北京' and positionName like 'python%'"#python
    cursor.execute(sql1)
    # print(cursor.fetchall()[0][0])
    python = len(cursor.fetchall())
    num.append(python)
    sql2 = "select  * from cities_job where  city='北京' and positionName like 'java%'"  # java
    cursor.execute(sql2)
    java = len(cursor.fetchall())
    num.append(java)
    sql3 = "select  * from cities_job where  city='北京' and positionName like 'c%'"  # python
    cursor.execute(sql3)
    c = len(cursor.fetchall())
    num.append(c)
    sql4 = "select  * from cities_job where  city='北京' and positionName like 'android%'"  # android
    cursor.execute(sql4)
    android = len(cursor.fetchall())
    num.append(android)
    for i in num:
        print(i)

def group_by():
    nums = []
    city = []
    db = pymysql.connect("localhost", "root", "1997", "lagouwang", charset='utf8')
    cursor = db.cursor()
    sql = ' select count( *),city  from cities_job  GROUP BY city having count(*) >=1 '#得到城市工作数量
    cursor.execute(sql)
    for i in cursor.fetchall():
        nums.append(i[0])
        city.append(i[1])
    print(nums)
    print(sum((nums)))
    print(city)
    map = Map("中国it专业分布图", width=1200, height=600,title_color='#fff')
    map.add("", city, nums, maptype='china', visual_text_color="#000",symbol_size=10, is_visualmap=True,is_label_show=True)
    map.render('2.html')

if __name__ == '__main__':
    set_china() #添加中文
    # pie_chart()
    # wordl_cloud()
    # education_chart()
    group_by()
