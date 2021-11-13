from bs4 import BeautifulSoup
import requests
import csv
import time

HEADER = ['開催日','開場時間','開始時間','会場']
url = 'https://www.njpw.co.jp/schedule'

with open('njpw_events.csv','w',encoding='utf_8_sig') as f:

    writer = csv.writer(f)
    writer.writerow(HEADER)

while True:

    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.content, 'html.parser')
    events = soup.find_all('div',class_='eventInfo')
    next_page = soup.find('li',class_='next')

    with open('njpw_events.csv','a',encoding='utf_8_sig') as f:

        writer = csv.writer(f)

        for event in events:
            eventInfo = (event.find_all('dd'))
            date = eventInfo[0].text
            place = eventInfo[1].text

            row = date.split()
            row.append(place)

            writer.writerow(row)

    if bool(next_page) == False:
        break
    
    url = next_page.a.get("href")
    time.sleep(1)