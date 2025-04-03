# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:24:08 2025

@author: tuesv

매장 수와 한국인 인구수 비교
매장 수와 외국인 인구수 비교
매장 수와 업종별 종사자 수 비교
업종별 => 상위 5개 업종
"""

import pandas as pd
import folium
import json

seoul_stat = pd.read_excel('./files/seoul_MGC_stat.xlsx', thousands=',')

# 서울시 시군구 행정 경계 지도 파일(.geojson)
file_path = './maps/seoul_sgg.geojson'
seoul_geo = json.load(open(file_path, encoding='utf-8'))

choropleth = folium.Map(location=[37.573050, 126.979189],
                    tiles='Cartodb dark_matter',
                    zoom_start=11)

folium.Choropleth(geo_data=seoul_geo,
                  data=seoul_stat,
                  columns=['시군구명', '건설업'],
                  fill_color='YlOrBr',
                  fill_opacity=0.7, 
                  line_opacity=0.5,
                  key_on='properties.SIG_KOR_NM').add_to(choropleth)

choropleth.save('건설업.html')

