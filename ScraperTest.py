from selenium import webdriver
import time
import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://ShrijanK:dummyPassword1234@cluster0.wfpuf.mongodb.net/DprogDb?retryWrites=true&w=majority")

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

URL = 'https://www.ctvnews.ca/health/coronavirus/tracking-every-case-of-covid-19-in-canada-1.4852102'

# Selenium Part
driver.get(URL) #Driver Fetches the URL

while True: #A While so that it runs every 24 hours

    total_height = int(driver.execute_script("return document.body.scrollHeight")) #Returns the total height of the document

    for i in range(1, total_height, 500): #Scrolls till the end of the website slowly
        driver.execute_script("window.scrollTo(0, {});".format(i))
        time.sleep(1) #Sleeps for 1 second after scrolling

    search = driver.find_elements_by_tag_name("td")

    casesList = []

    for val in search:
        if (val.text != ''):        
            casesList.append(val.text)

    collection = ['British Columbia', 'Alberta', 'Saskatchewan', 
                'Manitoba','Ontario','Quebec','New Brunswick',
                'Nova Scotia', 'Prince Edward Island','Newfoundland and Labrador',
                'Yukon','Northwest Territories','Nunavut']


    totalValList = casesList[5: :9] #[start : stop : skip ]

    mydb = client["DprogDb"]


    for i in range(len(collection)):
        myCol = mydb[collection[i]]
        myDict = {"Date": (datetime.datetime.today().strftime('%m/%d/%Y')), "Total Cases": totalValList[i]}

        x = myCol.insert_one(myDict)   


    client.close()

    driver.quit()

    time.sleep(86400)




    




