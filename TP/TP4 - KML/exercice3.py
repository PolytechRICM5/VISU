#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice3</name>\n'
)

for line in file :
    word = line.split()
    print(
        '<Placemark>\n'
        '<name>' + word[0] + ' : ' + word[3] + 'M hab.</name>\n'
        '<Point>\n'
        '<coordinates>' + word[1] + ',' + word[2] + '</coordinates>\n'
        '</Point>\n'
        '</Placemark>\n'
    )

print(
'</Document>\n'
'</kml>\n'
)

file.close();
