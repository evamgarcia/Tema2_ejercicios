import math 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        if self.x > 0 and self.y > 0:
            print("{] son del primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} son del segundo cuadrante".format(self))
        elif self.x < 0 and self.y <0:
            print("{} son del tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{}  son del cuarto cuadrante".format(self))
        else:
            print("{} esta sobre el origen".format(self))
    
    def vetor(self, p):
        print("el vecto entre {} y {} es ({}, {}".format(self, p, p.x - self.x, p.y - self.y))
