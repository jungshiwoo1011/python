# http://www.mois.go.kr/

import csv
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc

font_path = "python_data_A/csv_data/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp = []
yp_select = []
yp_names = []


for row in data :
    yp.append(row)
    # if area in row[0]:
    #     for i in row[3:]:
    #         yp.append(int(i))
del yp[0:2]
for i in yp:
    for j in range(3, len(i)):
        i[j] = int(i[j])

# print(yp)
for i in range(2):
    area = input("지역명 입력 : ")
    yp_names.append(area)
    for local in yp:
        if area in local[0]:
            yp_select.append(local[3:])
    # if "용문" in i[0]:
    #     print(i)

plt.title("양평군 인구분포도")
plt.style.use('ggplot')
for m in range(2):
    plt.plot(yp_select[m], label=yp_names[m])
plt.legend()
plt.show()