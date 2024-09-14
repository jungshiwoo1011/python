import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
yp_top = []
yp_rank = []

for row in data :
    yp_top.append(row)

del yp_top[0:2]

for i in range(len(yp_top)):
    del yp_top[i][1:3]
    yp_top[i][0] = yp_top[i][0][:-12]
    for j in range(1, len(yp_top[i][1:]) + 1):
        yp_top[i][j] = int(yp_top[i][j])

for top in yp_top:
    temp = []
    temp.append(top[0])
    temp.append(top.index(max(top[1:])))
    temp.append(max(top[1:]))
    yp_rank.append(temp)

yp_sort = [[], [], []]

for kkk in yp_rank:
    for y in range(len(kkk)):
        yp_sort[y].append(kkk[y])

print(yp_rank, yp_sort)

colors('black', )

plt.rc('font', family= 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.barh(yp_sort[0], yp_sort[2], color = colors, label = yp_sort[1])
plt.legend()
plt.show()