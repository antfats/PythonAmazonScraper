import requests
import smtplib
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com/DJI-Batteries-Camera-Gimbal-Accessories/dp/B07CTHT5SR/ref=sr_1_17?keywords=drone&qid=1570470783&refinements=p_72%3A1248963011%2Cp_36%3A1253564011&rnid=386491011&sr=8-17'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

title = soup2.find(id="productTitle").get_text()

price = soup2.find(id="priceblock_ourprice").get_text()

price = price.replace(',', '')
price = price.replace('$', '')
price = float(price[0:5])

if(price < 700):
    send_mail()



print(price)
print(title.strip())
