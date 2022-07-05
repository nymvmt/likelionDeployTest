import requests
from bs4 import BeautifulSoup
from webtoon_c import extract_info
import csv

file = open('webtoon_c.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","author","rate"])  #가장 위의 카테고리(?) 행을 지정한 것


final_result = []

# 우리가 정보를 얻고 싶어하는 URL
for page in range(1,11):
    WT_URL = f"https://comic.naver.com/webtoon/weekdayList?week=wed"
# get 요청을 통해 해당 페이지 정보를 저장
    WT_html = requests.get(WT_URL)
# bs4 라이브러리를 통해 불러온 html을 우리가 원하는 형태로 파싱
    WT_soup = BeautifulSoup(WT_html.text,"html.parser")


    WT_list_box = WT_soup.find("ul", {"class":"img_list"})
    WT_list = WT_list_box.find_all("li")

    final_result += extract_info(WT_list)

for result in final_result:
    row =[]
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rate'])
    writer.writerow(row)

print(final_result)
