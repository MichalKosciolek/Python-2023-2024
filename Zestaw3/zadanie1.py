import json

with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

trams = {}
lines = [int(tramwaj['linia']) for tramwaj in data['tramwaje']]

for i in range(len(lines)):
    for j in range(len(data['tramwaje'][i]['przystanek'])):
        trams.setdefault(lines[i], []).append(data['tramwaje'][i]['przystanek'][j]['nazwa'])

stops = {}
stops_set = set()
for i in trams:
    for j in range(len(trams[i])):
        trams[i][j] = trams[i][j][:-3]
        stops_set.add(trams[i][j])
    trams[i] = tuple(trams[i])
    stops[i] = len(trams[i])

sorted_stops = dict(sorted(stops.items(), key=lambda x: x[1], reverse=True))

for i in sorted_stops:
    print("Nr linii: ", i, " l. przystanków: ", sorted_stops[i])

print("Liczba wszystkich przystanków: ", len(stops_set))

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
    json.dump(trams, file, ensure_ascii=False, indent=4)