# Que3

class Father:
    def property(self):
        print("Father has property")

    def business(self):
        print("Father has business")

class Son(Father):
    def study(self):
        print("Son is studying")

class Daughter(Father):
    def dance(self):
        print("Daughter is dancing")

class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild play games")