from bs4 import BeautifulSoup
import requests

# 사이트 접속 -> F12 -> 네트워크 -> 헤더에서 User-Agent 정보 볼 수 있음
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
html = requests.get(url=base_url, headers=header_user).text

req = requests.get(base_url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

lst_all = lst50 + lst100

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a")
    singer = i.select_one(".ellipsis.rank02 a")
    album = i.select_one(".ellipsis.rank03 a")
    print(f"[순위] {rank}")
    print(f"제목: {title.text}")
    print(f"가수: {singer.text}")
    print(f"앨범: {album.text}")