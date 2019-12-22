import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.flipkart.com/dell-14-3000-core-i3-7th-gen-4-gb-1-tb-hdd-ubuntu-inspiron-3481-laptop/p/itm466e453c2270b?pid=COMFHTHRNDH3EZ2E&lid=LSTCOMFHTHRNDH3EZ2EL4GUOF&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=c675987d-be25-4656-8d23-d4c30a7fff4c.COMFHTHRNDH3EZ2E.SEARCH&ppt=sp&ppn=sp&ssid=dcocho8plc0000001577000517793&qH=1867cf4d208e7007"
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/79.0.3945.79 Chrome/79.0.3945.79 Safari/537.36"}
page=requests.get(URL, headers=headers)
def check_price():
    soup1=BeautifulSoup(page.content, 'html.parser')
    soup2=BeautifulSoup(soup1.prettify(), 'html.parser') 
    title=soup2.find(class_="_35KyD6").get_text()
    price=soup2.find(class_="_1vC4OE _3qQ9m1").get_text()
    price=price.strip()[1:]
    price_converted=""
    for v in price:
        if(v==","):
            continue
        else:
            price_converted+=v
    price_converted=float(price_converted)
    if(price_converted>20000):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("yjain8059@gmail.com", "rxswrtomoazloudk")
    subject="Congrats price of your product fell down!!"
    body="Check flipkart link https://www.flipkart.com/dell-vostro-15-core-i3-7th-gen-4-gb-1-tb-hdd-windows-10-home-3568-laptop/p/itmfdqwegz6fzxte?pid=COMFDQWEXH7JY8PB&lid=LSTCOMFDQWEXH7JY8PB2P8P7O&marketplace=FLIPKART&spotlightTagId=BestsellerId_6bo&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=484b1154-dbdc-47c0-b6d8-361588342ac9.COMFDQWEXH7JY8PB.SEARCH&ppt=sp&ppn=sp&ssid=s0np1m1tsw0000001576998309632&qH=1867cf4d208e7007"
    msg=f"Subject:{subject}\n\n\n{body}"
    dest_mail="yash3121999@gmail.com"
    server.sendmail("yjain8059@gmail.com",dest_mail,msg)
    print("HEY EMAIL HAS BEEN SENT TO: ",dest_mail)
    server.quit()

check_price()