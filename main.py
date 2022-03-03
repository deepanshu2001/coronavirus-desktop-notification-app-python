# Desktop notification app in python  that  will tell you about corona virus stats of a particular country
import datetime
import time
import requests
from plyer import notification # used to create notifications on laptop
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    
    print("Please! Check your internet connection")

if (covidData != None):
    data = covidData.json()['Success']
    
    
    while(True):
        notification.notify(
            
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  
            
            timeout  = 50
        )
        
        time.sleep(60)
