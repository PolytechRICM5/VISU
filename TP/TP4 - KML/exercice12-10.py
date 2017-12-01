#!/usr/bin/python3

file = open("data-tp2/cities.txt", "r");

print (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'<Document>\n'
'<name>Exercice10</name>\n'
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
'<color>ff0069ff</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ff0069ff</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="2">\n'
'<LineStyle>\n'
'<color>ff00ffff</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ff00ffff</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="3">\n'
'<LineStyle>\n'
'<color>ff00ff00</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ff00ff00</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="4">\n'
'<LineStyle>\n'
'<color>ffff6900</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ffff6900</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="5">\n'
'<LineStyle>\n'
'<color>ffff0069</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ffff0069</color></PolyStyle>\n'
'</Style>\n'
)
print (
'<Style id="6">\n'
'<LineStyle>\n'
'<color>ffff8bed</color>\n'
'<width>1</width>\n'
'</LineStyle>\n'
'<PolyStyle><color>ffff8bed</color></PolyStyle>\n'
'</Style>\n'
)

color=0
for line in file :
    word = line.split()
    print(
        '<Placemark>\n'
            '<name>' + word[0] + ' : ' + word[3] + 'M hab.</name>\n'
            '<styleUrl>#' + str(color%7) + '</styleUrl>\n'
            '<Polygon>\n'
                '<extrude>1</extrude>\n'
                '<altitudeMode>relativeToGround</altitudeMode>\n'
                '<outerBoundaryIs>\n'
                    '<LinearRing>\n'
                        '<coordinates>\n'
                            + str(float(word[1])+0.3*float(word[3])) + ',' + str(float(word[2])+0.2*float(word[3])) + ',100000\n'
                            + str(float(word[1])+0.3*float(word[3])) + ',' + str(float(word[2])-0.2*float(word[3])) + ',100000\n'
                            + str(float(word[1])-0.3*float(word[3])) + ',' + str(float(word[2])-0.2*float(word[3])) + ',100000\n'
                            + str(float(word[1])-0.3*float(word[3])) + ',' + str(float(word[2])+0.2*float(word[3])) + ',100000\n'
                            + str(float(word[1])+0.3*float(word[3])) + ',' + str(float(word[2])+0.2*float(word[3])) + ',100000\n'
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
    color+=1

print(
'</Document>\n'
'</kml>\n'
)

file.close();
