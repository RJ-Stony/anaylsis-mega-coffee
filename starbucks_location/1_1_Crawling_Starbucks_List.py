# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv
"""

# 크롤링을 이용한 서울시 스타벅스 매장 목록 데이터 생성
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.istarbucks.co.kr/store/store_map.do?disp=locale'
driver.get(url)

# webdriver로 ‘서울’ 버튼 요소를 찾아 클릭
# 1. '서울' 버튼 요소를 찾아
seoul_btn = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'

# 2. driver.find_element()를 이용
# css_selector, seoul_btn

# 3. click()
driver.find_element('css selector', seoul_btn).click()

# webdriver로 ‘전체’ 버튼 요소를 찾아 클릭
all_btn = '#mCSB_2_container > ul > li:nth-child(1) > a'

# click()
driver.find_element('css selector', all_btn).click()

# BeautifulSoup으로 HTML 파서 만들기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

'''
<li class="quickResultLstCon" 
    style="background:#fff" 
    data-lat="37.501087" 
    data-long="127.043069" 
    data-index="0" 
    data-name="역삼아레나빌딩" 
    data-code="3762" 
    data-storecd="1509" 
    data-hlytag="null">	
    <strong data-store="1509" 
            data-yn="N" 
            data-name="역삼아레나빌딩" 
            data-my_siren_order_store_yn="N">역삼아레나빌딩  
        </strong>
    <p class="result_details">서울특별시 강남구 언주로 425 (역삼동)<br>1522-3232</p>	
    <i class="pin_general">리저브 매장 2번</i>
</li>
'''

# select를 이용해 quickResultLstCon를 class명으로 가지는 li 태그 모두 가져오기
starbucks_soup_list = soup.select('li.quickResultLstCon')
len(starbucks_soup_list)
starbucks_store = starbucks_soup_list[0]

# 스타벅스 매장 정보 샘플 확인
name = starbucks_store.select('strong')[0].text.strip()
lat = starbucks_store['data-lat'].strip()
long = starbucks_store['data-long'].strip()
store_type = starbucks_store.select('i')[0]['class'][0][4:]
address = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
tel = str(starbucks_store.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]

print(f'찾으시는 매장은 {name}점이며,\n위치는 위도 {lat}도, 경도 {long}도\n즉, {address}에 위치해있습니다.\n매장은 {store_type} 타입이며, 매장 번호는 {tel}입니다.')

# 서울시 스타벅스 매장 목록 데이터
# 매장명, 위도, 경도, 주소, 전화번호
starbucks_list = []

for item in starbucks_soup_list:
    name = item.select('strong')[0].text.strip()
    lat = item['data-lat'].strip()
    long = item['data-long'].strip()
    store_type = item.select('i')[0]['class'][0][4:]
    address = str(item.select('p.result_details')[0]).split('<br/>')[0].split('>')[1]
    tel = str(item.select('p.result_details')[0]).split('<br/>')[1].split('<')[0]
    starbucks_list.append([name, lat, long, store_type, address, tel])
    
columns = ['매장명', '위도', '경도', '타입', '주소', '전화번호']
seoul_starbucks_df = pd.DataFrame(starbucks_list, columns=columns)

seoul_starbucks_df.info()
seoul_starbucks_df.to_excel('./files/seoul_starbucks_list.xlsx', index=False)
