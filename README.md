# ☕ MegaCoffee Location Analysis

메가커피 매장이 어디에, 왜, 얼마나 분포되어 있는지  
데이터 수집부터 시각화까지 한 번에 분석하는 공간입니다.

---

## 📁 구성 파일

```
megacoffee_location/
├── 1_1_Crawling_MGC_List.py          # 메가커피 매장 크롤링 (공식 웹사이트)
├── 1_2_edit_OpenData_Download.py     # 공공데이터포털 상권 정보 전처리
├── 2_data.py                         # 매장 + 상권 데이터 병합 및 저장
├── 3_1_map.py                        # folium 지도 시각화 생성
├── 3_2_location_visualization.py     # 업종별/지역별 밀도 시각화
├── *.html                            # 지도 시각화 결과 파일들
└── files/, maps/                     # 보조 데이터/이미지 폴더
```

---

## 🔍 분석 흐름

1. **매장 데이터 수집**
   - `1_1_Crawling_MGC_List.py`  
     → 메가커피 웹사이트에서 모든 지점 위치를 수집 (주소, 이름, 위도/경도 등)

2. **상권 데이터 병합**
   - `1_2_edit_OpenData_Download.py`  
     → 공공데이터포털에서 상권/행정구역 정보를 전처리

3. **데이터 통합**
   - `2_data.py`  
     → 수집된 매장 정보와 행정구역 데이터를 병합하여 분석용 데이터프레임 생성

4. **지도 시각화**
   - `3_1_map.py`  
     → `folium` 기반으로 전국 매장 위치를 HTML 지도에 표시

5. **상권 중심 분석**
   - `3_2_location_visualization.py`  
     → 업종별 밀도 분석 (도매소매업, 건설업 등), choropleth 지도 생성

---

## 🌐 시각화 결과 (예시 파일)

- `MGC_choropleth.html` : 메가커피 지점의 밀도 분포
- `top5.html` : 업종별 밀도 top5 시각화
- `전문서비스업(top4).html` 등 : 업종별 분석 결과

👉🏻 HTML 파일들은 브라우저에서 직접 열어볼 수 있습니다.

---

## 🛠 사용 기술

- `Python 3.12+`
- `pandas`, `beautifulsoup4`, `selenium`
- `folium`, `geopandas`, `matplotlib`
- 공공데이터포털 및 웹 크롤링 기반 데이터 수집

---

## 🧭 활용 포인트

- 상권 분석: 메가커피 매장이 어디에 많이 몰려 있는지 파악
- 입지 전략: 신규 매장 후보지 탐색
- 경쟁 분석: 특정 업종과의 밀접도 확인

---

## 📌 참고 사항

- 공공데이터 사용 시 최신 버전으로 갱신 필요
- 크롤링 대상 페이지 구조 변경 시 코드 수정 필요
