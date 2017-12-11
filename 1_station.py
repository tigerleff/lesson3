import csv

# Learn Python
# Задания для недели 3
# Остановки
# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.

with open('stations.csv', 'r', encoding="utf-8") as f:
    stations = []
    streets = {}
    count = 0
    num_line = 0
    for line in f.readlines()[1:]:
        num_line += 1

        sline = line.split(';')
        station = sline[1].split(',')[0]
        street = sline[4]

        if street not in streets:
            streets[street] = []

        if station not in streets[street]:
            streets[street].append(station)

        counts = len(streets[street])
        if len(streets[street]) > count:
            count = len(streets[street])
            max_station_street = street
                #print(street)

print('Больше всего остановок на улице >>> ' + max_station_street)
print('Количество станций на ' + max_station_street + ' ' + str(count))
print('Количество останововк ' + str(num_line))





