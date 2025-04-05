"""
매장 수와 한국인 인구수 비교
매장 수와 외국인 인구수 비교
매장 수와 업종별 종사자 수 비교
업종별 => 상위 5개 업종
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Selenium으로 브라우저 열기
driver = webdriver.Chrome()
driver.get("https://www.mega-mgccoffee.com/store/find/")
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

name_list = soup.select('div.cont_text_inner b')
names = [name.text.strip() for name in name_list]

address_list = soup.select('div.cont_text_inner.cont_text_info')
addresses = [addr.text.strip().split('\t')[0] for addr in address_list]

filtered_indices = [i for i, addr in enumerate(addresses) if addr.startswith('서울')]

filtered_names = [names[i] for i in filtered_indices]
filtered_addresses = [addresses[i] for i in filtered_indices]

filtered_gus = [addr.split()[1] for addr in filtered_addresses]

phone_list = soup.select('div.cont_text_inner.cont_text_info')
phones = [phone.text.strip().split('\t')[-1] for phone in phone_list]
filtered_phones = [phones[i] for i in filtered_indices]

df = pd.DataFrame({
    '매장명': filtered_names,
    '주소': filtered_addresses,
    '시군구명': filtered_gus,
    '전화번호': filtered_phones
})

df.to_excel('./files/seoul_MGC_list.xlsx', index=False)
