from plyer import notification
import time
import requests
# import json
from bs4 import BeautifulSoup

def NotifyMe(title,message):
    notification.notify(
            title = title,
            message = message,
            app_icon = "Assets/coronavirus.ico",
            timeout=15
        )
def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        htmldata = getData("https://www.mohfw.gov.in/")
        # print(htmldata)
        
        soup = BeautifulSoup(htmldata,'lxml')
        
        #find table and make them list from html data
        datastr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            datastr += tr.get_text()
        datastr = datastr[1:]
        itemstr = (datastr.split("\n\n"))   
        
        State = ['Gujarat','Maharashtra','Delhi']
        for item in itemstr[0:33]:
            statelist = item.split("\n")
            if statelist[1] in State:
                # print(statelist)
                nTitle = "Total cases of COVID-19"
                nText = f"State: {statelist[1]}\nTotal Cases : {statelist[2]}\nDischarged : {statelist[3]}\nDeaths : {statelist[4]}"
                NotifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3600)