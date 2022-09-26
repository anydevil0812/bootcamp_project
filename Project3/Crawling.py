# 공공데이터 포털 국회 국회사무처_의안 정보 오픈 API 크롤링
import re
from bs4 import BeautifulSoup
import requests
from Cloud import MakeCloud

url = 'http://apis.data.go.kr/9710000/BillInfoService2/getBillInfoList'
params ={'ServiceKey' : '디코딩키',
         'numOfRows' : '50', 'pageNo' : '1',
         'ord' : 'A01', 'start_ord' : '18', 'end_ord' : '21', 'bill_name' : '기후'}

# OPEN API를 이용하여 데이터 추출
response = requests.get(url, params=params) # UTF-8 코드 형식로 데이터가 불러와짐
soup = BeautifulSoup(response.content.decode('utf-8'), 'xml') # 한글로 보기 편하게 디코딩
final_text = soup.select('summary') # summary 태그 안에 있는 내용만 추출

# 불필요한 텍스트 제거
final_text = str(final_text) # 정규식을 적용하기 위하여 bs4.element.ResultSet -> str로 변환
final_text = re.sub('([,.!?·？\"\'])', '', final_text) # 특수문자 제거
final_text = re.sub('<.+>', '', final_text) # <> 태그 제거
print(final_text)

Cloud1 = MakeCloud()

Cloud1.wc(final_text)