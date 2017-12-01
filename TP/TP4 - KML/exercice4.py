#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

year = 2000

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice4</name>\n'
)

for line in file :
    word = line.split()
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

print(
'</Document>\n'
'</kml>\n'
)

file.close();
