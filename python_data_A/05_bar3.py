import csv
import matplotlib.pyplot as plt

f = open('python_data_A\csv_data\yp_mf.csv', 'r', encoding='utf8')
data = csv.reader(f)
m = []
f = []

result = []
for row in data:
    if '양평읍' in row[0]:
        # print(row)
        # for i in row[3:104]:
        #     m.append(int(i))
        # for i in row[106:]:
        #     f.append(int(i))

        for i in range(0, 101):
            m.append(-int(row[(i+3)]))
            f.append(int(row[-(i+1)]))

f.reverse()
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=150)
plt.rc('font', family= 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title("양평군 양평읍 성별분표")
plt.barh(range(101), m, label = "남성")
plt.barh(range(101), f, label = "여성")
plt.legend()
plt.show()