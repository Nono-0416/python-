import requests
import urllib.request as req
import bs4

number = str(input("請輸入代號:"))

url = "https://tw.stock.yahoo.com/quote/" + number + ".TW"
response = req.urlopen(url)
html = bs4.BeautifulSoup(response)

#股票名稱
name = html.find("h1",{"class":"C($c-link-text) Fw(b) Fz(24px) Mend(8px)"})
#股價
price = html.find("span",{"class":"Fz(32px)"})
#漲跌
change = html.find("span",{"class":"Fz(20px)"})
#漲跌符號
s = ""

if html.find("span",{"class":"Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-down)"}):
    s = "-"
elif html.find("span",{"class":"Fz(20px) Fw(b) Lh(1.2) Mend(4px) D(f) Ai(c) C($c-trend-up)"}):
    s = "+"
else:
    s = ''

result = (name.text + '：' + "股價:" + price.text + " 漲跌:" + s + change.text)

#LINE API
url = 'https://notify-api.line.me/api/notify'
token = '' #輸入自己的token
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}

data = {
    'message':result   # 設定要發送的訊息
}

data = requests.post(url, headers=headers, data=data)
