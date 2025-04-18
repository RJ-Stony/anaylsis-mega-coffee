import pandas as pd

# 시군구 목록 데이터 불러오기
seoul_sgg = pd.read_excel('./files/seoul_sgg_list.xlsx')
seoul_MGC = pd.read_excel('./files/seoul_MGC_list.xlsx')

MGC_sgg_count = seoul_MGC.pivot_table(index='시군구명',
                                      values='매장명',
                                      aggfunc='count').rename(columns={'매장명': '매장수'})

# 서울시 시군구 목록 데이터에 스타벅스 매장 수 데이터를 병합
seoul_sgg = pd.merge(seoul_sgg, MGC_sgg_count, on='시군구명', how='left')

# 서울시 시군구 목록 데이터에 서울시 시군구별 인구통계 데이터 병합
seoul_sgg_pop = pd.read_excel('./files/sgg_pop.xlsx')
seoul_sgg = pd.merge(seoul_sgg, seoul_sgg_pop, on='시군구명', how='left')
seoul_sgg

# 서울시 시군구 목록 데이터에 서울시 시군구별 사업체 수 통계 데이터를 병합
seoul_sgg_biz = pd.read_excel('./files/top5.xlsx')
seoul_sgg = pd.merge(seoul_sgg, seoul_sgg_biz, on='시군구명', how='left')
seoul_sgg

# 병합 결과 엑셀로 저장
seoul_sgg.to_excel('./files/seoul_MGC_stat.xlsx', index=False)
