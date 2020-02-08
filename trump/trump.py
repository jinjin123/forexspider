#-*- coding:utf-8 -*-
#python3.6+
import json
import os
import datetime
import MySQLdb
import hashlib
import random
import requests
import time
import twint

today = datetime.datetime.now().strftime('%Y-%m-%d')

c = twint.Config()
c.Username = "realDonaldTrump"
c.Proxy_type="http"
c.Proxy_host="localhost"
c.Proxy_port=3213
#c.Search = "twint"
c.Since=today
c.Output = "trump.json"
c.Store_json = True
twint.run.Search(c)


url="http://api.fanyi.baidu.com/api/trans/vip/translate"
appid = '20191105000353104' 
secretKey = 'w92s1mq62xYvVAW3Ldlo' 
salt = random.randint(32768, 65536)

def get_tra_res(q,fromLang='en',toLang='zh'):
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    data = {
        "appid": appid,
        "q": q,
        "from": fromLang,
        "to" : toLang,
        "salt" : str(salt),
        "sign" : sign,
    }
    #print(data)
    res = requests.post(url, data=data)
    trans_result = json.loads(res.content).get('trans_result')[0].get("dst")
    return trans_result


mq2=MySQLdb.connect(host="192.168.50.100",port=3306,user="root",passwd="zxc123",db="spiderflow",charset='utf8')
cur = mq2.cursor()
with open("trump.json","rb") as b:
    for line in b.readlines():
        tmp = json.loads(line)
        sql="select tag from trump where tag = '%s'" % str(tmp["created_at"])
        row = cur.execute(sql)
        if row == 0:
            #trs = get_tra_res(tmp["tweet"].split("https")[0])
            trs = get_tra_res(tmp["tweet"])
            #if  "pic" in trs:
            #    break
            #elif "https" in trs:
            #    break
            #else:
            cur.execute('insert into trump (content,tag,time,exttime) values (%s,%s,%s,%s)', (trs,str(tmp["created_at"]),(datetime.datetime.strptime(tmp["date"]+" "+tmp["time"],"%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d %H:%M:%S"),tmp["date"]))
            mq2.commit()
        #limit api
        time.sleep(2)



if (os.path.exists("./trump.json")):
    os.remove("trump.json")

