#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

year = 2000

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice5</name>\n'
)

table = []

for line in file :
    table.append(line)

i = 0;
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

while i < len(table) :
    prev = table[i-1].split()
    word = table[i].split()
    print(
        '<Placemark>\n'
        '<name>path</name>\n'
        '<TimeSpan>\n'
        '<begin>' + str(year) + '</begin>\n'
        '</TimeSpan>\n'
        '<LineString>\n'
        '<extrude>1</extrude>\n'
        '<tesselate>1</tesselate>\n'
        '<altitudeMode>absolute</altitudeMode>\n'
        '<coordinates>\n'
        + prev[1] + ',' + prev[2] + ',2357\n'
        + word[1] + ',' + word[2] + ',2357\n'
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

print(
'</Document>\n'
'</kml>\n'
)

file.close();
