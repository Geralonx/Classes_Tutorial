# Dieses File soll ein paar Beispiele von mehrfachen Vererbungen zeigen.
# Ob man dies genau so machen sollte und ob diese Vererbungsstruktur und dieses 
# Design sinnvoll ist, darüber kann man sich sicher streiten. Der Sinn dieses 
# Files ist lediglich eine größere Vererbeungsstruktur zu zeigen, um die 
# Handhabung der Argumente der einzelnen Klasse zu beschreiben.

# Hinweis: Man könnte _3DObj auch von _2DShape erben lassen, wenn man sagt, dass 
# ein 3D Objekt eine erweiterung einer 2DShape ist. Aber ich wollte hier einmal 
# zeigen was passiert, wenn man aus verschiedenen  Klassen mit der gleichen 
# Base-Klasse erbt.

import math

class BaseShape(): # Base-Shape-Class
    def __init__(self, corners, edges, color=None):
        # Alle Shapes können eine Farbe, eine Anzahl an Kanten und Ecken haben.
        # Selbst ein Kreis hätte 0 Edges und 0 Corners, welche dann aus einer
        # Circle Klasse übergeben werden müsste.

        # Weitere Kwargs sind an dieser Stelle ausgeschlossen, da dies die 
        # Grundklasse ist und Nichts weitergeleitet werden muss.
        # (Die übergeordnete Klasse wäre type/object)
        self.corners = corners
        self.edges = edges
        self.color = color

    def __str__(self):
        # Die Dunder-str-Methode ist so allgemein designed, dass diese für alle
        # zukünftigen Kindklassen verwendet werden kann. Es ist eine allgemeine
        # Darstellung einer Klasse mit den Elternklassen und den Attributen.

        # Man könnte __bases__ noch mit __mro__ ersetzten, um die ganze Struktur
        # zu erhalten. Mit __bases__ bekommt man eben nur die direkte Elternklasse.
        msg = '*'*80
        msg += f"\nDiese Instanz ist von der Klasse: {self.__class__.__name__}\n"
        msg += f"\nDiese Klasse hat folgende Elternklassen"
        msg += ''.join([f"\n\t{element.__qualname__}" for element in self.__class__.__bases__])
        msg += f"\n\nSie hat folgende Attribute:"
        msg += ''.join([f"\n\t{key}: \t{value} \t| ({type(value)})" for key, value in self.__dict__.items()])
        msg += '\n'
        msg += '*'*80
        return msg

class _2DShape(BaseShape): 
    def __init__(self, **kwargs):
        # Eine 2D-From hat keine eigenen besonderen Argumente, da die Fläche und
        # die Ecken/Kanten abhängig vom Typ der From sind, welche in der spezifizierung
        # der _2DShape Klasse aufgefangen werden. Die super() Methode leitet die
        # Argumente weiter, welche in der Base-Klasse benötigt werden.
        super().__init__(**kwargs)

class _3DObj(BaseShape):
    def __init__(self, faces, depth, **kwargs):
        # Jede 3-Dimensionale Form hat eine Tiefe. Dementsprechend wird hier die
        # 'depth' und die 'faces' aufgefangen und in die Instanz eingetragen.
        # Die Argumente der Base-Klasse werden durch die kwargs aufgefangen und 
        # weitergeleitet.
        self.depth = depth
        self.faces = faces
        super().__init__(**kwargs)

class Rectangle(_2DShape):
    def __init__(self, height, width, corners=4, edges=4, **kwargs):
        # Ein Rechteck hat eine Höhe und Breit. Dies ist immer der Fall und gilt
        # für alle Arten von Rechtecken. Corners wird an dieser Stelle abgefangen
        # und neu in die kwargs eingetragen. 

        # Ein Rechteck hat Grundsätzlich 4 Ecken und 4 Kanten. Durch die weitere 
        # Verwendung in einem 3D-Shape können sich diese aber ändern. Deswegen 
        # können hier Defaultwerte gesetzt werden und in das kwargs-Dict 
        # eingetragen werden. Die Defaultwerte müssen deshlab extra so gesetzt 
        # werden, da im Falle der Vererbung in eine 3D-Shape sich ändern könnten.
        kwargs['corners'] = corners
        kwargs['edges'] = edges
        self.height = height
        self.width = width
        super().__init__(**kwargs)
        
    def area(self):
        # Die Fläche eines Rechtecks ist auch immer eineindeutig mittels Höhe*Breite
        # zu bestimmen. Die Oberfläche einer 3D-Shape wird in der deutschen Mathematik
        # zwar auch häufig mit A/Area abgekürzt, aber in diesem Fall spezifiziere ich,
        # dass dies bei den 3D-Shapes die 'surface' sein wird.
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side, **kwargs):
        # Ein Qudaraht ist ein spezielles Rechteckt, welches die gleiche Höhe wie
        # Breite hat. Da man ein Quadraht aber nur mit einer Seitenlänge definiert
        # Fange ich die Seitenlänge hier ab und trage sie auf Höhe und Breite des
        # Rechtecks ein.
        super().__init__(width=side, height=side, **kwargs)

class Cuboid(Rectangle, _3DObj):
    def __init__(self, **kwargs):
        # Ein Cuboid hat eine bezüglich eines 3D-Shapes keine besonderen Attribute.
        # Die Attribute setzten sich aus den height/width des Rectangles zusammen
        # und der depth aus dem 3D-Shape. Lediglich werden im super().__init__
        # die Corners, Edges und Faces gesetzt, da sich diese Bezüglich der
        # Defaultwerte des Rectangles unterschieden.
        super().__init__(corners=8, edges=12, faces=6, **kwargs)

    def surface(self):
        # Die Surface-Methode ist für alle Rectangles gültig. Für einen Cube muss
        # diese nicht abgeändert werden, auch wenn sie eventuell einfacher aussieht.

        # Hier könnte man auch für eine Seite die area()-Methode aufrufen, aber 
        # ich finde diese Darstellung eindeutiger, da man ansosnten nachsehen muss, 
        # wie die Area eigentlich definiert ist.
        a1 = self.height * self.width 
        a2 = self.height * self.depth
        a3 = self.width * self.depth
        return 2 * (a1 + a2 + a3)

    def volumen(self):
        # Die Volumen-Methode ist für alle Rectangles gültig. Für einen Cube muss
        # diese nicht abgeändert werden, auch wenn sie eventuell einfacher aussieht.
        return super().area() * self.depth

# Man könnte ein Cube auch aus der Square und _3DObj Klasse erstellen. Wenn man 
# sich die Cuboid Klasse anschaut, dann macht dies aber keinen Sinn, da die Cuboid
# Klasse bereits Inhalte hat, welche sich für einen Cube wiederholen würde. (Code-Reuse)
class Cube(Cuboid):
    def __init__(self, side, **kwargs):
        # Der Cube hat keine besonderen Argumente im Gegnsatz zum Rectangle.
        # Lediglich die Seitenlänge ist an allen Seiten gleich, weswegen an dieser
        # Stelle die 'side' auf alle Attribute des Rectangles zugewiesen wird.
        super().__init__(height=side, width=side, depth=side, **kwargs)


class Circle(_2DShape):
    def __init__(self, radius, **kwargs):
        # Ein Kreis ist mit einem Radius ausreichend definiert. Die weiteren Argumente
        # der Base Klasse werden wie zuvor auch als **kwargs weitergegeben.
        self.radius = radius
        super().__init__(corners=0, edges=0, **kwargs)

    def area(self):
        # Kreisfläche -> A = pi * r ** 2
        return math.pi * (self.radius ** 2)

class Sphere(Circle, _3DObj):
    def __init__(self, radius, **kwargs):
        # Die Kugel ist wie das Quadraht ein besonderer Fall. Der Radius des
        # Kreises beschreibt eine Kugel auch hinreichend. Eine 'depth' Tiefe
        # Gibt es an sich nicht. Ich bin kein Blender/3D-Model Experte, deswegen
        # weiß ich nicht, wie eine Kugel in solchen Programmen beschrieben wird.
        # Einfachheitshalber setzte ich die 'depth' einfach mal auf den radius.
        super().__init__(radius=radius, depth=radius, faces=1, **kwargs)

    def surface(self):
        # Kugeloberfläche -> A = 4 * (pi * r ** 2)
        # (pi * r **2) -> Circle Area
        return 4 * super().area()

    def volumen(self):
        # Kugelvolumen -> V = 4/3 * pi * r ** 3
        return 4/3 * (math.pi * (self.radius ** 3))


# --- --- Instanzierung --- --- #

# Cube und Square werden in gleicher Weise aufgerufen. Lediglich die 
# Weiterverarbeitung der Argumente wird anders behandelt.

square1 = Square(side=50, color='Red')
cube1 = Cube(side=10, color='Green')
print(Cube.__mro__)

cuboid1 = Cuboid(height=10, width=20, depth=30, color='Blue')
rectangle1 = Rectangle(height=10, width=20)

sphere1 = Sphere(10, color='Brown')

print(square1)
print(cube1)
print(rectangle1)
print(cuboid1)
print(sphere1)


print("*" * 10, "Square Area", "*" * 10)
print(square1.area())

print("*" * 10, "Cube Surface and Volumen", "*" * 10)
print(cube1.surface())
print(cube1.volumen())

print("*" * 10, "Cuboid Surface and Volumen", "*" * 10)
print(cuboid1.surface())
print(cuboid1.volumen())


print("*" * 10, "Sphere Surface and Volumen", "*" * 10)
print(sphere1.surface())
print(sphere1.volumen())



