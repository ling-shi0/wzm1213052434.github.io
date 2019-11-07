#coding=utf-8
from twilio.rest import Client
import json , requests , sys , time ,datetime

dir=r"C:\zhujibao\Domains\wangxiaoming.com.cn\public_html\send"

while True:
    dtime=datetime.datetime.now()
    kk=dtime.strftime("%H")
    if kk!="11":
        time.sleep(1)
        #print("here")
    else:
        oldfile=open(dir+r"\oldfile.txt","r")
        filething=oldfile.read()
        #print(type(filething))
        filelist=filething.split("\n")
        #print(filelist)
        #print(type(filelist))
        for i in filelist:
            thinglist=i.split()
            #print(thinglist)
            if(thinglist!=[]):
                jsonWeather=open(dir+"\_city.json",'r',encoding='utf-8')
                jsonread=json.load(jsonWeather)
                sname=thinglist[5]
                #print(sname)
                scode=""
                for s in jsonread:
                    if(sname==s["city_name"]):
                        scode=s["city_code"]
                #print(scode)
                url=r"http://t.weather.sojson.com/api/weather/city/"+scode
                
                response=requests.get(url)
                response.raise_for_status()
                
                weatherData=json.loads(response.text)
                w=weatherData["data"]
                s=w["wendu"]
                k="现在温度:"
                k+=s
                k+="℃"
                k+=" 天气："
                s+="to mo"+w["forecast"][0]["high"]
                
                s+="to mo"+w["forecast"][0]["low"]
                s+="to we："+w["forecast"][0]["type"]
                k+=w["forecast"][0]["type"]
                # Your Account SID from twilio.com/console
                account_sid = thinglist[1]
                # Your Auth Token from twilio.com/console
                auth_token  = thinglist[3]
                
                client = Client(account_sid, auth_token)
                #print(thinglist[7],thinglist[9],thinglist[10])
                message = client.messages.create(
                to=thinglist[7], 
                from_=thinglist[9]+" "+thinglist[10],
                body=k)
                
                #print(message.sid)
                #print(s)
        time.sleep(72000)
