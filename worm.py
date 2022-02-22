import requests
from bs4 import BeautifulSoup

# GET 網頁資料
r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")

# parser html
soup = BeautifulSoup(r.text, "html.parser")

# 選取 html 標籤中的目標
sel = soup.select("div.title a")

# 取出目標中的標題文字
for s in sel:
  print(s["href"], s.text)