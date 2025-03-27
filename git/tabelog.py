import urllib.request as req
import bs4
import urllib.error as err

page = 55
while True:
    print("頁數:",page)
    
    url = "https://tabelog.com/tw/osaka/rstLst/" + str(page) + "/?SrtT=rt"
    try:
        response = req.urlopen(url)
    except err.HTTPError:
        print("MAYBE LAST PAGE")
        break
    page = page + 1
    #josn.load:型態轉換
    html = bs4.BeautifulSoup(response)
    # 區塊.find/find_all(區塊名字, 篩選條件class/id)
    #a = html.find("a", {"class":"list-rst__name-main"})
    #print(a)
    rs = html.find_all("li", {"class":"list-rst"})
    for r in rs:
        en = r.find("a", {"class":"list-rst__name-main"})
        ja = r.find("small",{"class":"list-rst__name-ja"})
        s = r.find("b",{"class":"c-rating__val"})
        m = r.find_all("span",{"class":"c-rating__val"})
        # 屬性: 區塊["href"]
        # 一個型態可以擁有兩種東西 1. 專屬功能  2. 專屬值
        # 顯示內容(專屬值): 區塊.text
        print(en.text,ja.text)
        print("評價",s.text)
        print("午間",m[0].text)
        print("晚間",m[1].text)
        print(en["href"])
        print("-" * 30)
