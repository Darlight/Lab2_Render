"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

main.py
Proposito: Crear una linea dentro del framebuffer con las posibles optimizaciones
"""
from tezt import Render


bitmap = Render()
print(bitmap.glInit())
bitmap.glCreateWindow() 



#bitmap.Line(0,0,1,1)
#bitmap.Line(-1,-1,1,1)
#bitmap.Line(-1,0,0,1)
#bitmap.Line(1,0,0,1)
#bitmap.Line(1,0,-1,0)
#bitmap.Line(-1,0,1,0)
bitmap.Line(0,0,0,1)




bitmap.glFinish('out.bmp')