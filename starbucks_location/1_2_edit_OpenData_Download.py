# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:22:02 2025

@author: tuesv
"""

import pandas as pd

# 시군구별 주민등록인구 데이터: report.txt
sgg_pop_df = pd.read_csv('./files/report.txt', sep='\t', header=2)

columns = {
    '기간': 'GIGAN',
    '자치구': 'JACHIGU',
    '계': 'GYE_1',
    '계.1': 'GYE_2',
    '계.2': 'GYE_3',
    '남자': 'NAMJA_1',
    '남자.1': 'NAMJA_2',
    '남자.2': 'NAMJA_3',
    '여자': 'YEOJA_1',
    '여자.1': 'YEOJA_2',
    '여자.2': 'YEOJA_3',
    '세대': 'SEDAE',
    '세대당인구': 'SEDAEDANGINGU',
    '65세이상고령자': 'N_65SEISANGGORYEONGJA'
}

sgg_pop_df.rename(columns=columns, inplace=True)
sgg_pop_df.info()

# 필요없는 데이터 제거: 데이터 합계
df_filter = sgg_pop_df[sgg_pop_df['JACHIGU'] != '합계']

# 분석에 필요한 컬럼 선택
df_final = df_filter[['JACHIGU', 'GYE_1']]
df_final.columns = ['시군구명', '주민등록인구']

df_final.head()
df_final.to_excel('./files/sgg_pop.xlsx', index=False)

# 동별 사업체 현황 통계 데이터: report2.txt
biz_df = pd.read_csv('./files/report2.txt', sep='\t', header=2)

# 시군구동별 사업체 현황 데이터 추출
df_filter = biz_df[biz_df['동'] == '소계']

# 필요없는 컬럼 제거: '자치구', '계', '사업체수'만 필요
columns = ['자치구', '계', '사업체수']
df_final = df_filter[columns]
df_final.columns = ['시군구명', '종사자수', '사업체수']

# 인덱스 초기화
df_final = df_final.reset_index(drop=True)
df_final.to_excel('./files/sgg_biz.xlsx', index=False)

