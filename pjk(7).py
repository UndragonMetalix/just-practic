#№1
class Square:
    list = []
    def __init__(self, name):
        self.name = name
        self.list.append((self.name))

    def print_name (self):
        ("{}".format(self.name))

shape = Square("квадрат")
print(Square.list)

#№2

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def __repr__(self):
        return "{} на {} на {} на {}".format(self.s1, self.s1, self.s1, self.s1)
square = Square(29)
print(square)

#№3 

def AleJerik(p1, p2):
    return p1 is p2
print(AleJerik("a", "a"))
 