from bs4 import BeautifulSoup
import requests
import csv

HEADER = ['開催日','開場時間','開始時間','会場']

url = 'https://www.njpw.co.jp/schedule'
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
events = soup.find_all('div',class_='eventInfo')

with open('dates.csv','w',encoding='utf_8_sig') as f:

    writer = csv.writer(f)
    writer.writerow(HEADER)

    for event in events:
        eventInfo = (event.find_all('dd'))
        date = eventInfo[0].text
        place = eventInfo[1].text

        row = date.split()
        row.append(place)

        writer.writerow(row)