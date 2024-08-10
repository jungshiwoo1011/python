import csv
f = open('python_data_A\yp.csv', 'r', encoding='utf8')
data = csv.reader(f, delimiter=',')
print(f, type(f), data, type(data))
header = next(data)
print(header)

min = 0
min_day = ''
max = 0
max_day =''
my_min = 0
my_max = 0
my_day = "2008-10-11"

for row in data:
    row[0] = row[0].lstrip()
    if row[-2] == '' or row[-1] == '':
        pass
    else:
        row[-2], row[-1] = float(row[-2]), float(row[-1])
        if row[-2] < min:
            min = row[-2]
            min_day = row[0]
        if row[-1] > max:
            max = row[-1]
            max_day = row[0]
        if row[0] < my_day:
            my_max, my_min = row[-1], row[-2]
print(f"최저기온 : {min} 날짜 : {min_day}")
print(f"최고기온 : {max} 날짜 : {max_day}")
print(f"시우 최저기온 : {my_min} 시우 최고기온 : {my_max}")
f.close()