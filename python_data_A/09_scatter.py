import csv
import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 40],  s= [100, 200, 250, 300], c=range(4), cmap= 'cool')
# plt.colorbar()

# plt.show()


import random
x = list(range(0, 101))
y1 = []
size1 = []
y2 = []
size2 = []

f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
 
for i in data:
    if "양평읍" in i[0]:
        y1 = i[3:]
    if "용문면" in i[0]:
        y2 = i[3:]

for change in range(len(y1)):
    y1[change] = int(y1[change])
    y2[change] = int(y2[change])

size1, size2 = y1, y2
# for i in range(100):
#     x.append(random.randint(50, 100))
#     y.append(random.randint(50, 100))
#     size.append(random.randint(10, 100))
plt.style.use('ggplot')
# # plt.scatter(x, y, s = size)

# # plt.scatter(x, y, s = size, c = size, cmap = 'jet')

plt.scatter(x, y1, s = size1, c = size1, cmap = 'jet', alpha = 0.7)
plt.scatter(x, y2, s = size2, c = size2, cmap = 'jet', alpha = 0.7)

plt.colorbar()
plt.show()