import os 
import json
from matplotlib import dates
import pandas as pd
from bs4 import BeautifulSoup
from collections import OrderedDict, defaultdict
from datetime import date, timedelta
import ujson
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt
import requests

def main():

    # with open('rsi.json','r') as f:
        with open('test3.json','r') as y:
            
            
            data = pdr.get_data_yahoo(['AAPL'],'2000-01-18','2023-02-09')
            # data["returns"]=data.Close.pct_change()
            # data["log_returns"]=np.log(1+data["returns"])
            # data.dropna(inplace=True)
            print(data)
            # data2=ujson.load(y)
            # data=data.to_dict("records")
        
            # # data3 = ujson.load(f)
            # data=ujson.load(f)
            
            # url = 'https://www.alphavantage.co/query?function=ADX&symbol=AAPL&interval=daily&time_period=5&apikey=94SM4DAGQ024RW8N'
            # r = requests.get(url)
            # data = r.json()
            
            # with open('ADX.json','w') as js:
            #     ujson.dump(data, js, indent=4)

                
   
          
            # temp["DailyInfo"]=[]
            # ldates=[]
            # # datec=0
            # temp={}
            # temp["DailyInfo"]=[]
            # temper=data["Technical Analysis: RSI"]
           
          
                    
            # move=0
            # counter=0
            # for entry2 in reversed(data2['DailyInfo']):
            #     move+=1
            #     counter=0
            #     for key, value in temper.items():
            #         counter+=1
            #         if move!=counter:
            #             continue
            #         entry2.update({"RSI":float(value['RSI'])})
            #         break
            # temp={}
            # temp2={}
            
            # for entry in data2['DailyInfo']:
            #     entry["AROONOSC"].update(float(entry["AROONOSC"]))
            #     print(entry["AROONOSC"])
                
            # tempadjclose=""
            # tempclose=""
            # tempopen=""
            # temphigh=""
            # templow=""
            # tempvolume=""
            # tempreturn=""
            # templogreturn=""
            
            # count=0
            # for entry in data2['DailyInfo']:
                
            #         if(entry["EPS estimate"]=="None"):
            #             tempepsest=float(0.00)
            #         else:
            #             tempepsest=float(entry["EPS estimate"])
                    
            #         if(entry["surprise"]=="None"):
            #             tempsurprise=float(0.00)
            #         else:
            #              tempsurprise=float(entry["surprise"])
                        
            #         if(entry["surprise %"]=="None"):
            #             tempsurprisePer=float(0.00)
            #         else:
            #             tempsurprisePer=float(entry["surprise %"])

                    
                    
            #         tempdate=entry["Date"] 
            #         tempeps=float(entry["EPS"])
            #         tempemp=float(entry["EMA"])
            #         temprsi=float(entry["RSI"])
            #         temparoon=float(entry["AROONOSC"])
            #         tempslowd=float(entry["SlowD"])
            #         tempslowk=float(entry["SlowK"])
            #         tempfastk=float(entry["FastK"])
            #         tempfastd=float(entry["FastD"])
            #         tempmacsig=float(entry["MACD_Signal"])
            #         tempmacd=float(entry["MACD"])
            #         tempmachis=float(entry["MACD_Hist"])
            #         temproc=float(entry["ROC"])
            #         tempadjclose=entry["adj close"]
            #         tempclose=entry["close"]
            #         tempopen=entry["open"]
            #         temphigh=entry["high"]
            #         templow=entry["low"]
            #         tempvolume=entry["volume"]
            #         tempreturn=entry["return"]
            #         templogreturn=entry["logreturn"]

            #         entry.update({"Date":tempdate})
            #         entry.update({"surprise":tempsurprise})
            #         entry.update({"surprise %":tempsurprisePer})
            #         entry.update({"EPS":tempeps})
            #         entry.update({"EPS estimate":tempepsest})
            #         entry.update({"EMA":tempemp})
            #         entry.update({"RSI":temprsi})
            #         entry.update({"AROONOSC":temparoon})
                    
            #         entry.update({"SlowD":tempslowd})
            #         entry.update({"SlowK":tempslowk})
            #         entry.update({"FastK":tempfastk})
            #         entry.update({"FastD":tempfastd})
            #         entry.update({"MACD_Signal":tempmacsig})
            #         entry.update({"MACD":tempmacd})
            #         entry.update({"MACD_Hist":tempmachis})
            #         entry.update({"ROC":temproc})
                            
            #         entry.update({"adj close":tempadjclose})
            #         entry.update({"close":tempclose})
            #         entry.update({"open":tempopen})
            #         entry.update({"high":temphigh})
            #         entry.update({"low":templow})
            #         entry.update({"volume":tempvolume})
            #         entry.update({"return":tempreturn})
            #         entry.update({"logreturn":templogreturn})
               

                
                
            # move=0
            # counter=0
            # for entry in  data['DailyInfo']:
            #     move+=1
            #     counter=0
            #     for entry2 in reversed(data2['DailyInfo']):
            #         counter+=1
            #         if move!=counter:
            #             continue
            #         entry.update(entry2)
            #         break
            # print(data2)
                    
                    
            #     temp.update(entry)
            #     temp2.update([temp])
            # print(temp2)

            # tempEarn=""
            # tempSur=""
            # tempSurPer=""
            # tempEPSest=""
            # tempFiscal=""

            
            # move=0
            # counter=0
            # temp=data3['quarterlyEarnings']
            # temp2=data2['DailyInfo']
            
            
            # y=len(temp)-1
            # i=len(temp2)-1
            # print(i)
            # print(y)
            # for x in range(len(temp2)):
            #         Date=temp[y]['reportedDate']     
            #         Date2=temp2[i]['Date']
                    
            #         # print(Date,Date2)
                    
                    
                    
            #         if(Date==Date2 or Date=="2000-12-31"):
            #             if(Date=="2000-12-31"):
            #                 continue
            #             tempEPSest=temp[y]['estimatedEPS']
            #             tempEarn=temp[y]['reportedEPS']
            #             tempSur=temp[y]['surprise']
            #             tempSurPer=temp[y]['surprisePercentage']
            #             tempFiscal=temp[y]['fiscalDateEnding']
            #             y-=1
            #             print(temp[y])
                        
            #         temp2[i].update({"surprise":tempSur})
            #         temp2[i].update({"surprise %":tempSurPer})
            #         temp2[i].update({"EPS":tempEarn})
            #         temp2[i].update({"EPS estimate":tempEPSest})
            #         temp2[i].update({"fiscal Date End":tempFiscal})
            #         i-=1
                    
                
            
            # for entry2 in data2['DailyInfo']:
                
            #     for entry in data3['quarterlyEarnings']:
            #         Date=entry['reportedDate']     
            #         Date2=entry2['Date']
                    
                    
            #         if(Date==Date2):
                        # print(Date,Date2)
                        # tempEPSest=entry['estimatedEPS']
                        # tempEarn=entry['reportedEPS']
                        # tempSur=entry['surprise']
                        # tempSurPer=entry['surprisePercentage']
                        # tempFiscal=entry['fiscalDateEnding']
                        
                        
            #         entry2.update({"surprise":tempSur})
            #         entry2.update({"surprise %":tempSurPer})
            #         entry2.update({"EPS":tempEarn})
            #         entry2.update({"EPS estimate":tempEPSest})
            #         entry2.update({"fiscal Date End":tempFiscal})
            
            # # print(data2)
                    
            # tempadjclose=""
            # tempclose=""
            # tempopen=""
            # temphigh=""
            # templow=""
            # tempvolume=""
            # tempreturn=""
            # templogreturn=""
            
            # move=0
            # counter=0
            # for entry2 in data2['DailyInfo']:
            #     move+=1
            #     counter=0
            #     for entry in  data:
            #         counter+=1
            #         if move!=counter:
            #             continue
            #         tempadjclose=entry[('Adj Close', 'AAPL')]
            #         tempclose=entry[('Close', 'AAPL')]
            #         tempopen=entry[('Open', 'AAPL')]
            #         temphigh=entry[('High', 'AAPL')]
            #         templow=entry[('Low', 'AAPL')]
            #         tempvolume=entry[('Volume', 'AAPL')]
            #         tempreturn=entry[('returns', '')]
            #         templogreturn=entry[('log_returns', '')]
                    
                    
            #         entry2.update({"adj close":tempadjclose})
            #         entry2.update({"close":tempclose})
            #         entry2.update({"open":tempopen})
            #         entry2.update({"high":temphigh})
            #         entry2.update({"low":templow})
            #         entry2.update({"volume":tempvolume})
            #         entry2.update({"return":tempreturn})
            #         entry2.update({"logreturn":templogreturn})
            #         break
            
            # print(temp)


            # temp["DailyInfo"]=[]
            # start_dt = date(1996,4,17)
            # end_dt = date(2022,1,27)
            # weekdays = [6,7]
            # for dt in daterange(start_dt, end_dt):
            #     if dt.isoweekday() not in weekdays:
            #         day=dt.strftime("%Y-%m-%d")
            #         temp["DailyInfo"].append({"Date":str(day)})
                    # print(dt.strftime("%Y-%m-%d"))
                    


            # start_date = date(ldates[datec-1][0],ldates[datec-1][1],ldates[datec-1][2]) 
            # end_date = date(ldates[0][0],ldates[0][1],ldates[0][2])    # perhaps date.now()
            # delta = end_date - start_date   # returns timedelta
            # year,month,day=splitString(Date)
            # ldates.append([int(year),int(month),int(day)])
            # datec+=1
            # for i in range(delta.days + 1):
            #         day = start_date + timedelta(days=i)  
            #         temp["DailyInfo"].append({"Date":str(day)})


        # with open('test4.json','w') as js:
        #         ujson.dump(data2, js, indent=4)

      
      
def splitString(data):
    string=""
    for i in data:
        
        if i!="-":
            string=string+i 
    count=0
    year=""
    month=""
    day=""
    for i in string:
        if count < 4:
            year=year+i
        if count <6 and count>3:
            month=month+i
        if count >5 and count<8:
            day=day+i
        count=count+1
    return year, month, day
          
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

if __name__ == "__main__":
    main()    

