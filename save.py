from plyer import notification
import time
import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
now=today.strftime("%m/%d/%Y")

def notifyMe(title , message):
    notification.notify(
        title = title,
        #today = date.today(),
        message = message,
        app_icon= r"C:\Users\ASUS\Desktop\Shalu\icon.jpeg",
        timeout= 10
        )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
   # while True:
        #notifyMe("Corona Update", "lets stop this togther")
        myHtmlData = getData('https://prsindia.org/covid-19/cases')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        
        table= soup.find('table')
        
        table_rows = table.find_all('tr')
        
        
       

        row=[]
        for tr in table_rows[1:36]:
            td = tr.find_all('td')
            row.append([i.text for i in td])
            
             
        states=['Chandigarh','Uttar Pradesh','Punjab','Delhi']
        
        for i in row:
            dataList=i
            if dataList[1] in states:
                print(dataList)
                ntitle="Cases of COVID-19 in INDIA "+now
                nmessage= f"State : {dataList[1]}\nConfirmed cases : {dataList[2]}\nRecoveries : {dataList[4]}\nDeaths : {dataList[5]}"
                notifyMe(ntitle,nmessage)
                time.sleep(2)
   # time.sleep(60)
           
       

      
       
