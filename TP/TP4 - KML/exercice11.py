#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

year = 2000
nb_points = 100

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice11</name>\n'
)

print (
'<Style id="0">\n'
'<LineStyle>\n'
'<color>ff0000ff</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ff0000ff</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="1">\n'
'<LineStyle>\n'
'<color>cc0069ff</color>\n'
'<width>2</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>cc0069ff</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="2">\n'
'<LineStyle>\n'
'<color>aa00ffff</color>\n'
'<width>4</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>aa00ffff</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="3">\n'
'<LineStyle>\n'
'<color>8800ff00</color>\n'
'<width>8</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>8800ff00</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="4">\n'
'<LineStyle>\n'
'<color>66ff6900</color>\n'
'<width>16</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>66ff6900</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="5">\n'
'<LineStyle>\n'
'<color>44ff0069</color>\n'
'<width>32</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>44ff0069</color></PolyStyle>\n'
'</Style>\n'
)

table = []

for line in file :
    table.append(line)

i = 0
word = table[i].split()
print(
    '<Placemark>\n'
    '<name>' + word[0] + ' : ' + word[3] + 'M hab.</name>\n'
    '<TimeSpan>\n'
    '<begin>' + str(year) + '</begin>\n'
    '</TimeSpan>\n'
    '<Point>\n'
    '<coordinates>' + word[1] + ',' + word[2] + '</coordinates>\n'
    '</Point>\n'
    '</Placemark>\n'
)
year+=1
i+=1

color = 0
while i < len(table) :
    prev = table[i-1].split()
    word = table[i].split()
    lon = float(word[2]) - float(prev[2])
    lat = float(word[1]) - float(prev[1])
    print(
        '<Placemark>\n'
        '<name>path</name>\n'
        '<styleUrl>#' + str(color%6) + '</styleUrl>\n'
        '<TimeSpan>\n'
        '<begin>' + str(year) + '</begin>\n'
        '</TimeSpan>\n'
        '<LineString>\n'
        '<extrude>1</extrude>\n'
        '<tesselate>1</tesselate>\n'
        '<altitudeMode>relativeToGround</altitudeMode>\n'
        '<coordinates>'
    )
    for j in range(nb_points) :
        print(
            str(float(prev[1]) + lat * j / nb_points) + ',' + str(float(prev[2]) + lon * j / nb_points) + ',2357'
        )
    print (
        word[1] + ',' + word[2] + ',2357\n'
        '</coordinates>\n'
        '</LineString>\n'
        '</Placemark>\n'
    )
    year+=1
    print(
        '<Placemark>\n'
        '<name>' + word[0] + ' : ' + word[3] + 'M hab.</name>\n'
        '<TimeSpan>\n'
        '<begin>' + str(year) + '</begin>\n'
        '</TimeSpan>\n''<Point>\n'
        '<coordinates>' + word[1] + ',' + word[2] + '</coordinates>\n'
        '</Point>\n'
        '</Placemark>\n'
    )
    year+=1
    i+=1
    color+=1

print(
'</Document>\n'
'</kml>\n'
)

file.close();
