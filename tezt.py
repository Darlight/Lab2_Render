"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

tezt.py
Proposito: Un framebuffer simple para pintar un punto con modificaciones simples como:
- Cambiar de color de los puntos
- Crear un punto
- Modificaciones del tamaño de la venta principal
"""
#struc pack
# wikipedia bmp file format
import struct
#opcion = 0
def char(c):
    # un char que vale un caracter de tipo string
    return struct.pack('=c', c.encode('ascii'))

def word(c):
    #convierte el numero de posicion de pixel a 2 bytes
    return struct.pack('=h', c)

def dword(c):
    #4 bytes de la estructura de un framebuffer
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])

class Render(object):
    def __init__(self):
        #Tamanio del bitmap
        self.windowWidth = 0
        self.windowHeight = 0
        self.viewPortWidth = 0
        self.viewPortHeight = 0
        self.color = WHITE
        self.xPort = 0
        self.yPort = 0
        self.framebuffer = []
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
    #Basicamente __init__ ^ hace esta funcion, asi que cree esta funcion por estética
    
    def glInit(self):
        return "Bitmap creado... \n"

    def point(self, x, y):
        self.framebuffer[y][x] = WHITE

    def glCreateWindow(self, width, height):
        self.windowWidth = width
        self.windowHeight = height
        self.framebuffer = [
            [BLACK for x in range(self.windowWidth)]
            for y in range(self.windowHeight)
        ]

    def glViewPort(self, x, y, width, height):
        self.xPort = x
        self.yPort = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def glClear(self):
        self.framebuffer = [
            [BLACK for x in range(self.windowWidth)]
            for y in range(self.windowHeight)
        ]

    def glClearColor(self, r=0, g=0, b=0):
        self.framebuffer = [
            [color(r,g,b) for x in range(self.windowWidth)]
            for y in range(self.windowHeight)
        ]

    def glVertex(self, x, y):
        #Formula sacada de:
        # https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml
        newX = round((x + 1)*(self.viewPortWidth/2)) + self.xPort
        newY = round((y + 1)*(self.viewPortHeight/2)) + self.yPort
        #funcion point para optimar
        self.point(newX,newY)

    def glColor(self, r=0, g=0, b=0):
        #self.framebuffer[self.yPort][self.xPort] = color(r,g,b)
        #Cambiar los valores de 0-255 a 0-1
        self.color = color(r,g,b)
    def glLine(self, placement, ycardinal = True):
        #variables condicionales y misma formual del vertex
        position = ((placement + 1) * (self.viewPortHeight/2) + self.yPort) if ycardinal else ((placement+1) * (self.viewPortWidth/2) + self.xPort)
        return round(position)

    def Line(self,x0,y0,x1,y1):
        self.x0 = self.glLine(x0, False)
        self.x1 = self.glLine(x1, False)
        self.y0 = self.glLine(y0)
        self.y1 = self.glLine(y1)
        #dy = abs(y1 - y0)
        #dx = abs(x1 - x0)
        #dy > dx
        steep = abs(self.y1 - self.y0) > abs(self.x1 - self.x0)
        if steep:
            self.x0 , self.y0 = self.y0, self.x0
            self.x1, self.y1 = self.y1, self.x1
        if self.x0 > self.x1:
            self.x0, self.x1 = self.x1, self.x0
            self.y0, self.y1 = self.y1, self.y0
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset  = 0
        threshold = dx 
       
        self.y = self.y0
        # y = y1 - m * (x1 - x)
        for self.x in range(self.x0, self.x1):
            if offset >= threshold:
                self.y += 1 if self.y0 < self.y1 else -1
                threshold += 2 * dx
            if steep:
                 #render.point(round(x), round(y))
                self.point(self.y, self.x)

            else:
                #render.point(x), round(y))
                self.point(self.x,self.y)
                
            offset += dy * 2
            

    def glFinish(self, filename):
        f = open(filename, 'bw')
        # file header
        f.write(char('B'))
        f.write(char('M'))

        f.write(dword(14 + 40 + self.windowWidth * self.windowHeight * 3))

        f.write(dword(0))

        f.write(dword(14 + 40))

        # image header 
        f.write(dword(40))
        f.write(dword(self.windowWidth))
        f.write(dword(self.windowHeight))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.windowWidth * self.windowHeight * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.windowWidth):
            for y in range(self.windowHeight):
                f.write(self.framebuffer[y][x])
        f.close()





#Colores como constantes
GREEN = color(0, 255, 0)
RED = color(255, 0, 0)
BLUE = color(0, 0, 255)
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255) 

#bitmap es el producto final, debo hacer un  menu completo 
# 128, 64

