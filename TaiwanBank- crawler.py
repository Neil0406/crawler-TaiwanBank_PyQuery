#從  pyquery   引用  PyQuery 類別（通常第一個字為大寫）
from pyquery import PyQuery
#安裝外部模組，在指令內輸入 pip install pyquery


# url 目標網頁
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
print(url)

#取得網頁內的所有html原始碼內容
html = PyQuery(url)
#篩選出貨幣清單 
#篩選規則  標籤.分類1.分類     .text()預設函數，刪除標籤    .split() 把字串空格切開變list

name_list = html("div.hidden-phone.print_show").text().split()
#買價列表  class表格表示""  屬性表示  []     
bid_list = html('td.rate-content-cash.text-right[data-table = "本行現金買入"]').text().split()
#賣價列表
offer_list = html('td.rate-content-cash.text-right[data-table = "本行現金賣出"]').text().split()
#print(name_list)
#print(bid_list)
#print(offer_list)
#{"美金"：{"買價"：29,"賣價"：30},"港幣"：{}}

table = {}  #建立空表單，貨幣查詢表
#print(offer_list)
#價格表索引
price_idx = 0

for idx, name in enumerate(name_list):
    #如果索引是偶數
    if idx % 2 ==0:
        table[name] = {
            "bid": bid_list[price_idx] ,
            "offer": offer_list[price_idx]
        }
        #把價格索引 ＋1
        price_idx += 1
        print(table)
#print(table)

#取得輸入
target = input("請輸入一個貨幣名稱：")
#從查詢表取得貨幣資料
currency = table[target]

#print(currency)

report = f"{target},買價：{currency['bid']},賣價：{currency['offer']}"
print(report)





