import time
import requests
import pymysql
from bs4 import BeautifulSoup
import re
import telnetlib
url1 = 'http://www.kuaidaili.com/free/inha/'
page = 1
#获取代理,并报错数据库
def get():
    global page #发生这种情况的原因是因为只要您写入变量，该变量就会自动为函数本地化。
    db = pymysql.connect("localhost", "root", "1997", "ip", charset='utf8')
    cursor = db.cursor()
    while page < 10:
        url2 = url1 + str(page) + '/'
        r = requests.get(url2)
        if r.status_code == 200:
            s = BeautifulSoup(r.text,'html.parser')
            z = s.find_all('tr')
            l = len(z)
            for x in range(1,l):
                ip = re.findall('<td data-title="IP">(.*)</td>',str(z[x]))
                po = re.findall('<td data-title="PORT">(.*)</td>',str(z[x]))
                # print(ip,po)
                try:
                    sql = "insert into foregin_ip values('%s','%s')" % (ip[0],po[0])
                    cursor.execute(sql)
                    db.commit()
                except :
                    print("插入途中发现错误！")
                    cursor.rollback()
        page+=1
        time.sleep(1)#太快了，有点慌
    cursor.close()
    db.close()

#质量检验
def check():
    db = pymysql.connect("localhost", "root", "1997", "ip", charset='utf8')
    cursor = db.cursor()
    sql = 'select * from foregin_ip'
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        print(x[0])
        print(x[1])
        try:
            telnetlib.Telnet(x[0], port=x[1], timeout=30)
        except:
            # print('connect failed')
            print(x[0]+':'+x[1] + ' 无效了!')
            sql = "DELETE FROM foregin_ip WHERE Ip='%s'" % (x[0])
            cursor.execute(sql)
            db.commit()
        else:
            print('success')
            print(x[0] + ':' + x[1] + ' 有效!')
    cursor.close()
if __name__ == '__main__':
    check()


