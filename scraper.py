import requests
import smtplib
from bs4 import BeautifulSoup


URL = 'https://www.amazon.com/DJI-Batteries-Camera-Gimbal-Accessories/dp/B07CTHT5SR/ref=sr_1_17?keywords=drone&qid=1570470783&refinements=p_72%3A1248963011%2Cp_36%3A1253564011&rnid=386491011&sr=8-17'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(id="priceblock_ourprice").get_text()

    price = price.replace(',', '')
    price = price.replace('$', '')
    price = float(price[0:5])

    if(price < 1300):
        send_mail()


page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')
title = soup2.find(id="productTitle").get_text()
price = soup2.find(id="priceblock_ourprice").get_text()


print(price)
print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('antfats50@gmail.com', 'vuauhfryjdghduph')

    subject = 'The price fell down!'
    body = 'Check the link! https://www.amazon.com/DJI-Batteries-Camera-Gimbal-Accessories/dp/B07CTHT5SR/ref=sr_1_17?keywords=drone&qid=1570470783&refinements=p_72%3A1248963011%2Cp_36%3A1253564011&rnid=386491011&sr=8-17'

    msg = f"Subject: {subject} \n\n{body}"

    server.sendmail(
        'antfats50@gmail.com',
        'antfats@hotmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT")
    server.quit()


check_price()
