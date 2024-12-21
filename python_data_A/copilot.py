import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정
rcParams['font.family'] = 'Malgun Gothic'  # Windows의 경우 'Malgun Gothic' 사용

# CSV 파일 경로 설정
file_path = 'python_data_A/csv_data/yp_10.csv'

# CSV 파일 읽기
df = pd.read_csv(file_path)

# "양평읍" 데이터 추출
yangpyeong_eup = df.iloc[0]
# "용문면" 데이터 추출
yongmun_myeon = df[df.iloc[:, 0] == '용문면'].iloc[0]

# 연령별 인구 데이터 추출 (네번째 데이터부터 마지막 데이터까지)
age_groups = yangpyeong_eup.index[3:]
population_counts_yp = yangpyeong_eup.values[3:]
population_counts_ym = yongmun_myeon.values[3:]

# 문자열 데이터를 정수형 데이터로 변환 (쉼표 제거 후 변환)
population_counts_yp = [int(str(count).replace(',', '')) for count in population_counts_yp]
population_counts_ym = [int(str(count).replace(',', '')) for count in population_counts_ym]

# 항아리 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

# 양평읍 데이터
ax.barh(age_groups, population_counts_yp, color='blue', label='양평읍')
# 용문면 데이터 (음수로 변환하여 반대 방향으로 그리기)
ax.barh(age_groups, [-count for count in population_counts_ym], color='green', label='용문면')

# 그래프 설정
ax.set_xlabel('인구 수')
ax.set_title('양평읍과 용문면의 연령별 인구 구성비율')
ax.legend()

# 차트 보여주기
plt.show()