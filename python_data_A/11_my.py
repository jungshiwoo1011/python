import matplotlib.pyplot as plt
import csv

f = open('python_data_A/csv_data/saenuk.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []

# for row in data:
#     if '용문면' in row[0]:
#         for i in row[3: ]:
#             if ',' in i:
#                 i = i.replace(',', '')
#             result.append(int(i))


# plt.bar(range(len(result)), result)
# plt.show()

yp_all = []
# label_ages = ["0~9", "10~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~99", "100~"]
label_gen = ["청소년(10~19)", "청년(20~39)", "장년(40~59)", "노년(60~)"]
yp_gen = []

for i in data:
    yp_all.append(i)

for da in range(len(yp_all)):
    for change in range(len(yp_all[da][3:])):
        if "," in yp_all[da][change + 3]:
            yp_all[da][change + 3] = int(yp_all[da][change + 3].replace(",", ""))
        else:
            yp_all[da][change + 3] = int(yp_all[da][change + 3])
    #print(yp_all[da])

yp_gen.append(sum(yp_all[0][3:5]))
yp_gen.append(sum(yp_all[0][5:7]))
yp_gen.append(sum(yp_all[0][7:9]))
yp_gen.append(sum(yp_all[0][9:]))

plt.pie(yp_gen, labels = label_gen, autopct="%.1f%%")
plt.show()