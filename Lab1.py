"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

Lab1.py
Proposito: Crear una linea dentro del framebuffer con las posibles optimizaciones
"""
from tezt import Render
bitmap = Render()
print(bitmap.glInit())
bitmap.glCreateWindow()


bitmap.Line(165,380,185,360)
bitmap.Line(185,360,180,330)
bitmap.Line(180,330,207,345)
bitmap.Line(207,345,233,330)
bitmap.Line(233,330,230,360)
bitmap.Line(230,360,250,380)
bitmap.Line(250,380,220,385)
bitmap.Line(220,385,205,410)
bitmap.Line(205,410,193,383)
bitmap.Line(193,383,165,380)





bitmap.glFinish('out.bmp')