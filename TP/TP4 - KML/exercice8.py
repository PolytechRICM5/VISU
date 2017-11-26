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
            '<Polygon>\n'
                '<extrude>1</extrude>\n'
                '<altitudeMode>relativeToGround</altitudeMode>\n'
                '<outerBoundaryIs>\n'
                    '<LinearRing>\n'
                        '<coordinates>\n'
                            + str(float(word[1])+0.2) + ',' + str(float(word[2])+0.2) + ',10000\n'
                            + str(float(word[1])+0.2) + ',' + str(float(word[2])-0.2) + ',10000\n'
                            + str(float(word[1])-0.2) + ',' + str(float(word[2])-0.2) + ',10000\n'
                            + str(float(word[1])-0.2) + ',' + str(float(word[2])+0.2) + ',10000\n'   
                        '</coordinates>\n'
                    '</LinearRing>\n'
                '</outerBoundaryIs>\n'
            '</Polygon>\n'
        '</Placemark>\n'
    )

print(
'</Document>\n'
'</kml>\n'
)

file.close();
