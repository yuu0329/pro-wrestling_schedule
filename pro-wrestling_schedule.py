from os import write
from bs4 import BeautifulSoup
import requests
import csv

HEADER = ['開催日','開場時間','開始時間']

url = 'https://www.njpw.co.jp/schedule'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
events = soup.find_all('div',class_='eventInfo')

with open('dates.csv','w',encoding='utf_8_sig') as f:

    writer = csv.writer(f)
    writer.writerow(HEADER)

    for event in events:
        date = event.find('dd').text

        row = date.split()
        
        writer.writerow(row)