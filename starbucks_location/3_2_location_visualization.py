import pandas as pd
import folium
import json

seoul_stat = pd.read_excel('./files/seoul_sgg_stat.xlsx', thousands=',')

# 서울시 시군구 행정 경계 지도 파일(.geojson)
file_path = './maps/seoul_sgg.geojson'

seoul_geo = json.load(open(file_path, encoding='utf-8'))
seoul_geo['features'][0]['properties']

bubble = folium.Map(location=[37.573050, 126.979189],
                    tiles='Cartodb voyager',
                    zoom_start=11)

def style_function(feature):
    return {
        'opacity': 0.7,
        'weight': 2,
        'color': '#32734E',
        'fillOpacity': 0.1,
        'dashArray': '5, 5',
        }

folium.GeoJson(seoul_geo, style_function=style_function).add_to(bubble)

# 서울시 시군구별 스타벅스 평균 매장 수 계산
starbucks_mean = seoul_stat['매장수'].mean()

# 버블 지도로 시각화
for idx in seoul_stat.index:
    lat = seoul_stat.loc[idx, '위도']
    long = seoul_stat.loc[idx, '경도']
    count = seoul_stat.loc[idx, '매장수']
    
    if count > starbucks_mean:
        fillColor = '#243832'
    else:
        fillColor = '#296044'
    
    folium.CircleMarker(
        location=[lat, long],
        color='#FFFFFF',
        fill_color=fillColor,
        fill_opacity=0.7,
        weight=1.5,
        radius=count/2).add_to(bubble)

bubble.save('starbucks_bubble.html')

# 서울시 시군구별 스타벅스 매장 수를 단계구분도로 시각화
choropleth = folium.Map(location=[37.573050, 126.979189],
                    tiles='Cartodb dark_matter',
                    zoom_start=11)

folium.Choropleth(geo_data=seoul_geo,
                  data=seoul_stat,
                  columns=['시군구명', '매장수'],
                  fill_color='YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on='properties.SIG_KOR_NM').add_to(choropleth)

choropleth.save('starbucks_choropleth.html')
