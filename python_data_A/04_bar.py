import matplotlib.pyplot as plt
# plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7])
# plt.bar(range(6), [1, 2, 3, 5, 6, 7])

# plt.show()

import csv
f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []
for row in data:
    if '양평읍' in row[0]:
        for i in row[3:]:
            result.append(int(i))
            
plt.bar(range(101), result)
plt.barh(range(101), result)
plt.show()
