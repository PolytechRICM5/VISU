#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice13</name>\n'
)

for line in file :
    word = line.split()
    hexa = '{0:02x}'.format(int(float(word[3])/8.7*255))
    print(
        '<Placemark>\n'
            '<name>' + word[0] + ' : ' + word[3] + 'M hab.</name>\n'
            '<Style>\n'
                '<LineStyle>\n'
                    '<color>ff00'+str(hexa)+'ff</color>\n'
                    '<width>1</width>\n'
                '</LineStyle>\n'
                '<PolyStyle><color>ff00'+str(hexa)+'ff</color></PolyStyle>\n'
            '</Style>\n'
            '<Polygon>\n'
                '<extrude>1</extrude>\n'
                '<altitudeMode>relativeToGround</altitudeMode>\n'
                '<outerBoundaryIs>\n'
                    '<LinearRing>\n'
                        '<coordinates>\n'
                            + str(float(word[1])+1) + ',' + str(float(word[2])+0.6) + ',100000\n'
                            + str(float(word[1])+1) + ',' + str(float(word[2])-0.6) + ',100000\n'
                            + str(float(word[1])-1) + ',' + str(float(word[2])-0.6) + ',100000\n'
                            + str(float(word[1])-1) + ',' + str(float(word[2])+0.6) + ',100000\n'
                            + str(float(word[1])+1) + ',' + str(float(word[2])+0.6) + ',100000\n'
                        '</coordinates>\n'
                    '</LinearRing>\n'
                '</outerBoundaryIs>\n'
            '</Polygon>\n'
        '</Placemark>\n'
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
