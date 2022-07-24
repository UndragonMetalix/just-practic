#№1

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2
        
class Square:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2
    

a_rectangle = Rectangle(20,26)
a_square = Square(21,21)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())

#№2

class Square:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2
    
    def change_size(self, w, l):
        self.width = w
        self.len = l
        

a_square = Square(21,21)
print(a_square.calculate_perimeter())

a_square.change_size(35,35)
print(a_square.calculate_perimeter())

#№3

class Shape():
    def what_am_i(self):
        print("Я - фигура")    

class Square(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Rectangle(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4 

rectega = Rectangle(20)
saka_waka = Square(20, 35)

rectega.what_am_i()
saka_waka.what_am_i()


#№4

class Horse():
    def __init__(self, name, breed, owner):
        self.name = name 
        self.breed = breed 
        self.owner = owner
class Rider():
    def __init__(self, name):
        self.name = name  

Fred = Rider("Фред Генг")
Rainbow_Dash = Horse("Rainbow Dash","Лошадь",Fred)
print(Rainbow_Dash.owner.name)


