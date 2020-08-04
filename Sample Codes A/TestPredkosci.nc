(Z axis Unused)
(X0,Y0,Z0= Center, Center, Top)
(MATERIAL TYPE= STYRO FOAM)
(TESTOWANIE PREDKOSCI POSUWU NA STYROPIANIE GR 30-50mm)
(Wlozyc blok styropianu o dl min 400mm i gr 50mm)
(na styropianie zaznaczone cieciami beda posuwy od 25mm/min do 200mm/min co 50mm)
(przy F powyzej 100 nalezy trzymac reke na przycisku reset)
(UWAGA! Maszyna przed uruchomieniem programu ma byc w pozycji zerowej!)
N10 G90 G21
(GCODE START)
G00 X0 Y0
G00 X-10 Y25
G00 X0
G01 X50 F25
G01 Y15
G01 Y25
G01 X100 F50
G01 Y15
G01 Y25
G01 X150 F75
G01 Y15
G01 Y25
G01 X200 F100
G01 Y15
G01 Y25
G01 X250 F125
G01 Y15
G01 Y25
G01 X300 F150
G01 Y15
G01 Y25
G01 X350 F175
G01 Y15
G01 Y25
G01 X400 F200
G01 Y70 F100
G00 Y100
G00 X0
G00 Y0
