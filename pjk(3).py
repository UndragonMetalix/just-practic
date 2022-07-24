#№1
class Apple:
    def __init__(self, r, s, f, ww):
        self.red = r
        self.spoiled = s
        self.fresh = f
        self.withworm = ww

apple1 = Apple("красное", "не испорченное", "свежее","с червяком")
print(apple1.red)

apple2 = Apple("не красное","испорченное","не свежее","не с червяком")
print(apple2.spoiled)

apple3 = Apple("красное","не испорченное","свежее","не с червяком")
print(apple3.fresh)

apple4 = Apple("не свежее","не испорченное","не красное","с червяком")
print(apple4.withworm)

print(apple1,apple2,apple3,apple4)


#№2
import math 

class Circle:
    def __init__(self, r):
        self.radius = r

    def area (self):
        return self.radius ** 2 * math.pi

circle = Circle(5) 
print(circle.area())



#№3
class Triangle:
    def __init__(self, a, b):
        self.a = a 
        self.b = b  

    def area(self):
        return self.a * self.b / 2
triangle = Triangle(10, 15)
print(triangle.area())

#№4
class Hexagon:
    def __init__(self, st1, st2, st3, st4, st5, st6):
        self.st1 = st1
        self.st2 = st2
        self.st3 = st3
        self.st4 = st4
        self.st5 = st5 
        self.st6 = st6
    
    def calculate_perimeter(self):
        return self.st1 + self.st2 + self.st3 + self.st4 + self.st5 + self.st6
hexagon = Hexagon(4,4,4,4,4,4) 
print(hexagon.calculate_perimeter())