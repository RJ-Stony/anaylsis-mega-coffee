import pandas as pd
seoul_starbucks = pd.read_excel('./files/seoul_starbucks_list.xlsx', header=0)

# 스타벅스 주소 정보에서 시군구명 추출
sgg_names = []

for address in seoul_starbucks['주소']:
    sgg_names.append(address.split()[1])
    
seoul_starbucks['시군구명'] = sgg_names
seoul_starbucks.to_excel('./files/seoul_starbucks_list.xlsx', index=False)
